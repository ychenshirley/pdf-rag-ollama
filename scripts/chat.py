from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "chroma_db"
COLLECTION = "book"

SYSTEM = (
    "You are a helpful assistant. Answer ONLY using the provided context. "
    "If the answer is not in the context, say you don't know."
)

def rag_answer(llm, docs, question: str) -> str:
    context = "\n\n---\n\n".join(
        f"[page {d.metadata.get('page', '?')}] {d.page_content}" for d in docs
    )
    prompt = f"{SYSTEM}\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    return llm.invoke(prompt).content

def main():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vs = Chroma(
        persist_directory=DB_DIR,
        collection_name=COLLECTION,
        embedding_function=embeddings,
    )
    retriever = vs.as_retriever(search_kwargs={"k": 6})
    llm = ChatOllama(model="llama3.1:8b", temperature=0)

    print("RAG chat ready. Type 'exit' to quit.\n")
    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        docs = retriever.invoke(q)
        answer = rag_answer(llm, docs, q)

        print("\nAgent:", answer)
        print("\nSources:")
        for d in docs[:3]:
            print(f"- page {d.metadata.get('page', '?')}")
        print()

if __name__ == "__main__":
    main()