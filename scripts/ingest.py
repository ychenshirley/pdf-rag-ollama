import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

PDF_PATH = "data/book.pdf"
DB_DIR = "chroma_db"
COLLECTION = "book"

def main():
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"Missing PDF at {PDF_PATH}")

    print("Loading PDF...")
    docs = PyPDFLoader(PDF_PATH).load()
    print(f"Loaded {len(docs)} pages")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=150,
    )
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    print("Building Chroma index...")
    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR,
        collection_name=COLLECTION,
    )
    vs.persist()
    print(f"Done. Saved to {DB_DIR}/ (collection={COLLECTION})")

if __name__ == "__main__":
    main()