# services/assistant.py

from utils.embedding import get_embedding
from database.chroma_client import query_similar_docs
from database.faiss_index import search_index
from core.config import COMPLETION_MODEL
import openai

def generate_response(query: str) -> str:
    query_embedding = get_embedding(query)

    # Retrieve top documents from Chroma
    chroma_results = query_similar_docs(query_embedding.tolist(), n=5)
    documents = chroma_results["documents"][0]

    # Search in FAISS
    _, indices = search_index(query_embedding, k=5)
    faiss_docs = [documents[i] for i in indices[0]]

    context = "\n".join(faiss_docs)
    prompt = f"Answer the following question using the documents:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = openai.Completion.create(
        model=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=100
    )

    return response["choices"][0]["text"].strip()

