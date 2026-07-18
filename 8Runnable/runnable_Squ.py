from langchain_OpenAI import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()
prompt=PromptTemplate(
    
    template='Write a joke about {topic}',
    input_variable=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()
prompt2=PromptTemplate(
    template='Explain the following joke - {text}',
    input_variable=['text ']
)
chain=RunnableSequence(prompt,model,parser,prompt2,model,parser)
print(chain.invoke({'topic':'AI'}))