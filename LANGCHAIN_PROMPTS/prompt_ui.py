import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Load TinyLlama locally
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 300,
        "temperature": 0.5,
    }
)

model = ChatHuggingFace(llm=llm)

# UI
st.title("Research Paper Explainer")

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium",
        "Long (Detailed Explanation)"
    ]
)

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template="""
You are a research paper expert.

Explain the research paper: {paper}

Explanation Style: {style}
Explanation Length: {length}

Provide:
1. Main idea of the paper
2. Problem it solves
3. Key innovations
4. Simple example
5. Important applications

Make the explanation clear and structured.
"""
)

if st.button("Generate Explanation"):

    prompt = prompt_template.format(
        paper=paper_input,
        style=style_input,
        length=length_input
    )

    with st.spinner("Generating explanation..."):
        result = model.invoke(prompt)

    st.subheader("Explanation")
    st.write(result.content)