import re

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough
)
from langchain_core.output_parsers import StrOutputParser


main_chain = None


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"

    match = re.search(pattern, url)

    if not match:
        raise ValueError("Invalid YouTube URL")

    return match.group(1)


def load_video(url):
    global main_chain

    video_id = extract_video_id(url)

    transcript = YouTubeTranscriptApi().fetch(video_id)

    text = " ".join(chunk.text for chunk in transcript)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([text])

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        docs,
        embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k":4}
    )

    pipe = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        max_new_tokens=150,
        temperature=0.2,
        do_sample=False
    )

    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    prompt = PromptTemplate(
        template="""
You are a helpful assistant.

Answer ONLY from the transcript.

If the answer is not present in the transcript, say:

"I couldn't find that information in the transcript."

Transcript:
{context}

Question:
{question}

Answer:
""",
        input_variables=[
            "context",
            "question"
        ]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    parallel = RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
    )

    parser = StrOutputParser()

    main_chain = (
        parallel
        | prompt
        | llm
        | parser
    )


def ask_question(question):
    global main_chain

    if main_chain is None:
        return "Please load a video first."

    return main_chain.invoke(question)