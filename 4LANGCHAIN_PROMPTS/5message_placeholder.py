from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
chat_template =ChatPromptTemplate([
    ('system','you are helpful customer support agent'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.read())
    