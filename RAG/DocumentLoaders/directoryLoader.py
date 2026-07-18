from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader=DirectoryLoader(
    path='books',
    glob='*.pdf'
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(len(docs[0].page_content))
print(docs[0].metadata)
# docs=loader.load()
# for document in docs:
#     print(document.metadata) taake more time because we are using load 

# docs=loader.lazy_load()
# for document in docs:
#     print(document.metadata) taake quick time because we are using load 
