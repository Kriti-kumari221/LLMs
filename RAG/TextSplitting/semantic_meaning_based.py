# use Embedding vector
from langchain_experimental.text_splitter import SemantiChunker
from langchain_openai.embeddings import OpenAIEmbeddings
load_dotenv()
text_Splitter=SentimentChuncker(
    OpenAIEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)
sample=""
