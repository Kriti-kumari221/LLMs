#Document simalirity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embeddings=OpenAIEmbeddings(model="test-embeddings-3-large",dimensions=32)
documents=["virat kohili is an Indian Cricketer know for his aggrassive batting and leadership",
           "MS dhoni is a former Indian capitain famous for his calm demeanor and finishing skills",
           "Sachine tendulkar also known as the god of cricketer hold many batting records "
           ]
query="tell me about virat kohli"
doc_embeddings=embeddings.embed_documents(documents)
query_embedding=embeddings.embed_query(query)
score=cosine_similarity([query_embedding],doc_embeddings)[0]
index,score=sorted(list(enumerate(score)))
print(query)
print(documents[index])
print("Similarity Score is: ",score)



