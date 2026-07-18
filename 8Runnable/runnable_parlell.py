from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
load_dotenv()
prompt1=PromptTemplate(
    template="Generate a linkdin post {topic}",
    input_variable=['topic']
)
prompt2=PromptTemplate(
    template="Generate a tweet post {topic}",
    input_variable=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()
parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkdin': RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke({'topic':'AI'})
result=parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])