from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model='gpt-4',tempratures=1.5,max_completion_tokens=10)
#temp is usefor creative 1.5 is good
result =model.invoke("What is the capital of india")
print(result)