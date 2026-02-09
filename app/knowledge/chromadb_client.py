import os
import chromadb
from dotenv import load_dotenv

load_dotenv()

# Singleton client
_client = None

# Cache collections by name
_collections: dict[str, any] = {}


def get_chroma_client():
    global _client

    if _client is None:
        _client = chromadb.CloudClient(
            api_key=os.getenv("CHROMA_API_KEY"),
            tenant=os.getenv("CHROMA_TENANT"),
            database=os.getenv("CHROMA_DATABASE"),
        )

    return _client


def get_collection(name: str):
    """
    Get an existing Chroma collection by name (READ ONLY).
    Caches collections safely.
    """
    if name not in _collections:
        client = get_chroma_client()
        _collections[name] = client.get_collection(name=name)

    return _collections[name]


# Convenience wrappers (optional but nice)
def get_trustpartners_collection():
    return get_collection("trustpartners_sg")


def get_mom_collection():
    return get_collection("mom_sg")

