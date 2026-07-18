# read PDF files 
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('pdf')
docs=loader.load()
print(len(docs))
print(docs[0].page_content) #firstpage
print(docs[0].metadata)

# Mostly text image if scaned img not work 
# table :-PDFPlummerLoaders
# scanned img:-Unstructure pdf loader  
#image data:- PyPDFLoader
 