from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal

# Load LLM
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    }
)

# ---------------- Pydantic Model ----------------
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )

# Parsers
parser = PydanticOutputParser(pydantic_object=Feedback)
text_parser = StrOutputParser()

# ---------------- Classifier Prompt ----------------
prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback as either positive or negative.

Feedback:
{feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

classifier_chain = prompt1 | llm | parser

# ---------------- Positive Prompt ----------------
prompt2 = PromptTemplate(
    template="""
Write a thank-you message to the customer for the following positive feedback.

Feedback:
{feedback}
""",
    input_variables=["feedback"]
)

# ---------------- Negative Prompt ----------------
prompt3 = PromptTemplate(
    template="""
Write a polite apology message to the customer for the following negative feedback.

Feedback:
{feedback}
""",
    input_variables=["feedback"]
)

# ---------------- Branch ----------------
branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        prompt2 | llm | text_parser,
    ),
    (
        lambda x: x.sentiment == "negative",
        prompt3 | llm | text_parser,
    ),
    PromptTemplate(
        template="Could not determine the sentiment.",
        input_variables=[]
    )
    | llm
    | text_parser,
)

# ---------------- Final Chain ----------------
chain = classifier_chain | branch_chain

# Invoke
result = chain.invoke(
    {
        "feedback": "This is a terrible smartphone."
    }
)

print(result)