# database/chroma_client.py

import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("documents")

def add_documents(docs: list[str], embeddings: list[list[float]]):
    for i, (doc, emb) in enumerate(zip(docs, embeddings)):
        collection.add(
            ids=[f"doc_{i}"],
            documents=[doc],
            embeddings=[emb]
        )

def query_similar_docs(embedding: list[float], n: int = 5):
    return collection.query(query_embeddings=[embedding], n_results=n)
