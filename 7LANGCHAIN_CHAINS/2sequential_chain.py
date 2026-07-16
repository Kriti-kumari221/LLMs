# # topic->LLM->Report->llm->summary
# 2 llm we have to call 
# Application
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

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
    template ='Generate a detailed report on {topic}',
    input_variable=['topic']
)
prompt2=PromptTemplate(
    template="Generate a 5 pointer summary for the following text \n {text}",
    input_variable=['text']
)
parser=StrOutputParser()
chain=prompt1|llm|prompt2|llm|parser
result=chain.invoke({'topic':'Unemployment in india'})
print(result)
chain.get_graph()
#without chain 

# # Step 1: Create first prompt
# formatted_prompt1 = prompt1.format(topic="Unemployment in India")

# # Step 2: Generate report
# report = llm.invoke(formatted_prompt1)

# # Step 3: Parse report
# report = parser.invoke(report)

# # Step 4: Create second prompt
# formatted_prompt2 = prompt2.format(text=report)

# # Step 5: Generate summary
# summary = llm.invoke(formatted_prompt2)

# # Step 6: Parse summary
# summary = parser.invoke(summary)

# print("===== REPORT =====")
# print(report)

# print("\n===== SUMMARY =====")
# print(summary)
