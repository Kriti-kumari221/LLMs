from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptsTemplate
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
loader=TextLoader(r"E:\Langchain_Models\RAG\DocumentLoaders\cricket.txt" ,encoding='utf-8')
docs=loader.load()
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.5,
)

model = ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='wright a summary for the following poem \n {poem}'
)
parser=StrOutputParser()
chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)