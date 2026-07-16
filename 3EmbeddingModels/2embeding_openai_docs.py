from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
documents=["Delh is the capital of india ",
           "kolkata is the capital of best bengol "]
embeddings=OpenAIEmbeddings(model='text-embedding-3-large',dimmension=32)
result=embeddings.embed_documents(documents)
print(str(result))