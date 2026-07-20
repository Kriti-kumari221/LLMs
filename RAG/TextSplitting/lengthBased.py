# chunks->size
# no meaning no context
from langchain_text_splitters import CharacterTextSplitter
text="it splits based on individual characters (no meaningful boundaries like spaces or newlines). This often breaks words, so the chunks have no context or meaning. That's why CharacterTextSplitter is generally not recommended for LLM applications.from langchain_text_splitters import CharacterTextSplitter from langchain_text_splitters import CharacterTextSplitter"
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_text(text)
print(result)
# if we have pdf and in pdf we have 5 pages that time insted of using split text we use split document 