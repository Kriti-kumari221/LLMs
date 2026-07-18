#runnable passthrow is a special primitives that simply returns the input as output without modifying it 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnablePassThrough
load_dotenv()
passthrough=RunnablePassThrough()
print(passthrough.invoke({'name':'kriti'}))
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
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'linkdin': RunnableSequence(prompt2,model,parser)
})
finalChain=RunnableSequence(joke_gen_chain,parllel_chain)
print(finalChain.invoke({'topic':'cricket'}))
# result=parallel_chain.invoke({'topic':'AI'})
# result=parallel_chain.invoke({'topic':'AI'})
# print(result['tweet'])
# print(result['linkedin'])

