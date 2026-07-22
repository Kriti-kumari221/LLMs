# LangChain & LLM Learning Journey

Welcome to my **LangChain & Large Language Models (LLMs)** learning repository.

This repository documents my journey of learning and implementing various concepts of **LangChain**, **Retrieval-Augmented Generation (RAG)**, **Prompt Engineering**, **Vector Databases**, **Embeddings**, **Structured Outputs**, and **LLM Applications** through hands-on projects and experiments.

The goal of this repository is not just to learn theory but to build practical applications while exploring different LangChain components.

---

# Learning Roadmap

## 1️ LLM Basics

- Introduction to LLMs
- Different Chat Models
- Local vs Cloud LLMs
- HuggingFace Models
- OpenAI Models
- Google Gemini
- Prompting Basics

 Folder

```
1LLMs/
```

---

## 2️ Chat Models

Learning how different chat models work with LangChain.

Topics Covered

- ChatOpenAI
- ChatGoogleGenerativeAI
- HuggingFace Chat Models
- Local Chat Models

  Folder

```
2ChatModels/
```

---

## 3️ Embedding Models

Understanding how text embeddings convert text into vectors for semantic search.

Topics Covered

- OpenAI Embeddings
- HuggingFace Embeddings
- Similarity Search
- Vector Representations

 Folder

```
3EmbeddingModels/
```

---

## 4️ Prompt Engineering

Learning different prompt templates and prompting techniques.

Topics Covered

- PromptTemplate
- ChatPromptTemplate
- Message Placeholders
- Chat History
- Prompt Chaining

 Folder

```
4PromptEngineering/
```

---

## 5️ Structured Outputs

Generating structured responses using LangChain.

Topics Covered

- JSON Output
- Pydantic Output Parser
- TypedDict
- Structured Response Generation

 Folder

```
5Structure_output/
```

---

## 6️ Output Parsers

Parsing model outputs into different formats.

Topics Covered

- String Parser
- JSON Parser
- Pydantic Parser

 Folder

```
6Output_parsers/
```

---

## 7️ LangChain Chains

Learning how different chains work.

Topics Covered

- Simple Chain
- Sequential Chain
- Parallel Chain
- Conditional Chain

  Folder

```
7LANGCHAIN_CHAINS/
```

---

## 8️ Runnables

Understanding LangChain Expression Language (LCEL).

Topics Covered

- RunnableSequence
- RunnableLambda
- RunnableParallel
- RunnableBranch
- RunnablePassthrough

 Folder

```
8Runnable/
```

---

#  Main Project

##  YouTube Transcript AI Chatbot (RAG)

One of the practical projects built during this learning journey.

This project demonstrates how Retrieval-Augmented Generation (RAG) can be used to build an AI chatbot that answers questions from a YouTube video's transcript.

### Features

- Paste any YouTube video URL
- Automatically fetch transcript
- Split transcript into chunks
- Generate embeddings
- Store embeddings in FAISS
- Retrieve relevant context
- Answer using TinyLlama
- Modern Flask UI

---

##  Project Workflow

```
YouTube URL
      │
      ▼
Transcript API
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
TinyLlama
      │
      ▼
Generated Answer
```

---

##  Concepts Used

- Retrieval-Augmented Generation (RAG)
- FAISS
- HuggingFace Embeddings
- LangChain
- Prompt Templates
- RunnableParallel
- RunnableLambda
- RunnablePassthrough
- Flask
- Transformers
- TinyLlama

---

##  Project Preview

<img width="1583" height="952" alt="Screenshot 2026-07-22 122414" src="https://github.com/user-attachments/assets/79f6076b-294f-4b69-aff1-5b3e658f40ac" />

---

#  Technologies Used

- Python
- LangChain
- HuggingFace
- Transformers
- TinyLlama
- FAISS
- Flask
- HTML
- CSS
- JavaScript

---

#  Repository Structure

```
Langchain_Models/
│
├── 1LLMs/
├── 2ChatModels/
├── 3EmbeddingModels/
├── 4PromptEngineering/
├── 5Structure_output/
├── 6Output_parsers/
├── 7LANGCHAIN_CHAINS/
├── 8Runnable/
├── RAG/
│   ├── app.py
│   ├── chatbot.py
│   ├── templates/
│   ├── chroma_db/
│   ├── Retrievers/
│   ├── VectorStore/
│   └── TextSplitting/
│
├── requirements.txt
└── README.md
```

---

#  Learning Outcomes

Through this repository, I gained practical experience with:

- Large Language Models (LLMs)
- LangChain Framework
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Embedding Models
- Vector Databases
- LangChain Expression Language (LCEL)
- Runnable Components
- Output Parsers
- Chat Models
- Flask Integration
- Building End-to-End AI Applications

---

#  Future Work

- PDF Chatbot
- Website Chatbot
- Multi-Document RAG
- Hybrid Search
- Agentic AI
- LangGraph
- Memory
- Tool Calling
- MCP
- Ollama Integration
- Llama 3
- Multi-modal AI

---

 *This repository is a collection of my hands-on learning projects while exploring LangChain and Large Language Models.*
