from fastapi import APIRouter
from openai import OpenAI
from app.knowledge.chromadb_client import get_trustpartners_collection

router = APIRouter()


@router.get("/health")
def health():
    status = {
        "openai": "ok",
        "chromadb": "ok",
        "overall": "ok"
    }

    # Check ChromaDB
    try:
        collection = get_trustpartners_collection()
        collection.count()
    except Exception as e:
        status["chromadb"] = "error"
        status["chromadb_error"] = str(e)
        status["overall"] = "unhealthy"

    # Check OpenAI
    try:
        client = OpenAI()
        client.models.list()
    except Exception as e:
        status["openai"] = "error"
        status["openai_error"] = str(e)
        status["overall"] = "unhealthy"

    return status
