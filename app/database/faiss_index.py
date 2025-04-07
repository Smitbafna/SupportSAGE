# database/faiss_index.py

import faiss
import numpy as np
from core.config import EMBEDDING_DIM

index = faiss.IndexFlatL2(EMBEDDING_DIM)

def add_to_index(embeddings: list[np.ndarray]):
    for emb in embeddings:
        index.add(np.array(emb).reshape(1, -1))

def search_index(query: np.ndarray, k: int = 5):
    return index.search(query.reshape(1, -1), k)
