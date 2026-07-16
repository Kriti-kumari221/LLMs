from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
schemas = [
    ResponseSchema(name="Fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="Fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="Fact_3", description="Fact 3 about the topic")
]
parser = StructuredOutputParser.from_response_schemas(schemas)
template = PromptTemplate(
    template="""
Give 3 facts about {topic}.
{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)
prompt = template.invoke({"topic": "black hole"})
result = model.invoke(prompt)
print(result.content)
final_result = parser.parse(result.content)
print(final_result)