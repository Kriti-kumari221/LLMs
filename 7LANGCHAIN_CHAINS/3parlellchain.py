from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
# os.environ['HF_HOME']='D:/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    }
)
prompt1=PromptTemplate(
    template="Generate short and simple notes of the following \n{text}",
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="Generate 5 short question answer from the fllwing text \n {text}",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Merge the provided notes and ques into the a single document \n {notes} and {quiz}',
    input_variables=['notes','quiz']
)
parser=StrOutputParser()
parllel_chain=RunnableParallel({
    'notes':prompt1|llm|parser,
    'quiz':prompt2|llm|parser,
})
merge_chain=prompt3|llm|parser
chain=parllel_chain|merge_chain
text="Artificial Intelligence is the simulation of human intelligence by machines. It enables computers to learn, reason, and solve problems."
result=chain.invoke({'text':'text'})
