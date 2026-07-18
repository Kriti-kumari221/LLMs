#if we want different different action on the basis of one situation 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnablePassthrough,RunnableBranch
load_dotenv()
passthrough=RunnablePassThrough()
print(passthrough.invoke({'name':'kriti'}))
prompt1=PromptTemplate(
    template="Generate a linkdin post {topic}",
    input_variable=['topic']
)

model=ChatOpenAI()
parser=StrOutputParser()
prompt2=PromptTemplate(
    template='Explain the following joke - {text}',
    input_variable=['text ']
)

report_gen_chain=RunnableSequence(prompt1,model,parser)
# report_gen_chain=prompt1|model|parser we can use this syntax also 
branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
    
)
final_chain=RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic':'today news'}))
