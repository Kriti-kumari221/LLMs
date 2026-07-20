# Recursive character text technique
# \n\n,=> Paragraph  , \n =>line , - => word  ' ' => Charater all representation symboll
# it start with first paragraph if not able to build on para then start with like if line not then word if not word then character 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
text="it splits based on individual characters (no meaningful boundaries like spaces or newlines). This often breaks words, so the chunks have no context or meaning. That's why CharacterTextSplitter is generally not recommended for LLM applications.from langchain_text_splitters import CharacterTextSplitter from langchain_text_splitters import CharacterTextSplitter"
splitter=RecursiveCharacterTextSplitter (
    chunk_size=30,
    chunk_overlap=0,
)
result=splitter.split_text(text)
print(result)