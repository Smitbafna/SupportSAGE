# main.py

from fastapi import FastAPI
from api.routes import router
from utils.embedding import get_embedding
from database.chroma_client import add_documents
from database.faiss_index import add_to_index

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def load_initial_documents():
    sample_docs = [
        "FastAPI is a modern web framework for building APIs with Python.",
        "ChromaDB is a vector database optimized for AI embeddings.",
        "FAISS enables efficient similarity search and clustering of dense vectors.",
        "OpenAI provides APIs for embedding, completion, and other AI services.",
        "Retrieval-Augmented Generation (RAG) enhances AI with contextual documents."
    ]
    embeddings = [get_embedding(doc) for doc in sample_docs]
    add_documents(sample_docs, [e.tolist() for e in embeddings])
    add_to_index(embeddings)
