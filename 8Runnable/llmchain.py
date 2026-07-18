from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
llm = OpenAI(
    model_name="gpt-3.5-turbo-instruct",
    temperature=0.7
)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)
chain=LLMChain(llm=llm, prompt=prompt)
topic=input("Enter topic")
output=chain.run(topic)
print(output)