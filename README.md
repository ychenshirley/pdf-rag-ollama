# PDF RAG with Ollama (Local, Free)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-black)
![LangChain](https://img.shields.io/badge/LangChain-1.x-orange)
![Chroma](https://img.shields.io/badge/Vector%20DB-Chroma-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-purple)

A simple local Retrieval-Augmented Generation (RAG) project:
- Ingest a PDF book into a local vector database (Chroma)
- Ask questions using a local Ollama model (e.g. Llama 3.1 8B)
- Print source pages used for each answer

> Everything runs locally on your machine (no paid API calls).  
> Don’t commit copyrighted PDFs to a public repo.

---

## Demo (example)
After ingesting, run chat and ask:

**Question1**
> What is this book about in 2–3 sentences? Mention the author’s main goal. 

**Example output1**
Agent: This book is about designing data-intensive applications, covering various aspects of distributed systems, transactions, and database systems. The author, Martin Kleppmann, aims to share his knowledge and experience gained from working on large-scale data infrastructure to help readers avoid common mistakes and develop better software. His main goal is to make profound technical ideas accessible to everyone, enabling them to create more effective and efficient applications.

Sources:
- page 400
- page 455
- page 612

**Question2**
**Example output2**
Agent: Based on the provided context, here are five main themes of this book:

* The importance of clarity in system architecture by being clear about data derivation
* The dual use of technology for good or bad purposes and its impact on society
* Maintaining software systems, including legacy systems, is a significant cost factor
* Understanding the principles behind successful data systems to navigate the diverse landscape of technologies
* Finding useful ways of thinking about data systems, including their algorithms, trade-offs, and scalability requirements

Sources:
- page 407
- page 4
- page 188

---

## Requirements
- macOS (works on any OS, but this repo is tested on macOS)
- Python 3.11+ (3.12 OK)
- [Ollama](https://ollama.com/) installed

## Setup

### 1. Clone
```bash
git clone git@github.com:ychenshirley/pdf-rag-ollama.git
cd 
```

### 2. Create virtual env + install deps
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U langchain langchain-community langchain-ollama langchain-text-splitters chromadb pypdf
```

### 3. Pull Ollama models
```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

## Usage

### 1. Put your PDF here
Place your book at ```data/book.pdf```

### 2. Ingest the PDF into a local vector DB
```bash
python scripts/ingest.py
```
### 3. Chat with your book 
```bash
python scripts/chat.py
```

Type ```exit``` to quit.