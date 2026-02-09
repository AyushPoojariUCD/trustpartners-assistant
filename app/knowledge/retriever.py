from typing import Any
from app.knowledge.chromadb_client import get_trustpartners_collection

def retrieve_context(collection: Any, query: str, k: int = 4) -> str:
    # print("[Retriever] Query received:", query)
    # print("[Retriever] Top K:", k)

    results = collection.query(
        query_texts=[query],
        n_results=k,
        include=["documents"]
    )

    # print("[Retriever] Raw results keys:", results.keys())

    documents = results.get("documents", [[]])[0]

    # print(f"[Retriever] Retrieved {len(documents)} documents")

    # for i, doc in enumerate(documents):
    #     print(f"\n--- Document {i+1} ---")
    #     print(doc[:300])

    # if not documents:
    #     print("[Retriever] No documents found")
    #     return ""

    return "\n\n".join(documents)