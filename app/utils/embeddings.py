# utils/embedding.py

import openai
import numpy as np
from core.config import OPENAI_API_KEY, EMBEDDING_MODEL

openai.api_key = OPENAI_API_KEY

def get_embedding(text: str) -> np.ndarray:
    response = openai.Embedding.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return np.array(response['data'][0]['embedding'])
