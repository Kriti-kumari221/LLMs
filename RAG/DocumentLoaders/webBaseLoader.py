# # extract page from weppage 
# # request , BeautifulSoup  it use two types to load internaly 
# for bloags article or public static website 
# if it's havy then dot work 
from langchain_community.document_loaders import WebBaseLoader

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptsTemplate
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

url="https://www.flipkart.com/boxman-men-vest/p/itmf7ff212541fe1?pid=VESHNZZCETEZMDTU&lid=LSTVESHNZZCETEZMDTUVDAMHP&marketplace=FLIPKART&store=clo%2Fqfl%2Fwp7%2Fzpk&srno=b_1_1&otracker=browse&fm=organic&iid=en_4CKFQa-TwDDx3eshwKU9quu6TDLhYxzITUf1grPMkX6MzsRvqmIfVPObhJ920jYtFlSFjS36OYVOIEbN8CSX7p0mJJuD0J5dl5vp4ebx4eAf8STtMVq_RvzrVBrve21S&ppt=browse&ppn=browse&ssid=s1k4r2b5j40000001784375944407&ov_redirect=true"

loader=WebBaseLoader(url)
docs=loader.load()
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.5,
)

model = ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Give the answer of following Question  {question} from the following text \n {text}'
    input_variables=['question','text']
)
parser=StrOutputParser()
chain=prompt|model|parser
print(chain.invoke({'question':'What is th peak brightnes of this product? ', 'text':docs[0].page_content}))
