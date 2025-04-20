# 🤖 SupportSAGE

**SupportSAGE** is an intelligent question-answering system powered by OpenAI embeddings and Retrieval-Augmented Generation (RAG). It combines **FastAPI**, **ChromaDB**, and **FAISS** to deliver accurate, context-aware responses using stored document knowledge.

---

## 📁 Project Structure

```
SupportSAGE/
│
├── core/
│   └── config.py              # Configuration (API keys, model names, dimensions)
│
├── utils/
│   └── embedding.py           # Generates embeddings using OpenAI
│
├── database/
│   ├── chroma_client.py       # Handles ChromaDB operations
│   └── faiss_index.py         # FAISS indexing and search
│
├── services/
│   └── assistant.py           # Main logic to generate AI responses
│
├── api/
│   └── routes.py              # API endpoint definitions using FastAPI
│
├── main.py                    # App entry point; loads documents and starts server
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```

---

## ⚙️ Features

- 🔍 **Semantic Search**: Uses OpenAI embeddings and FAISS for vector-based document retrieval.
- 🧠 **Context-Aware QA**: Implements RAG to generate answers grounded in relevant documents.
- ⚡ **FastAPI Interface**: Clean, modern API endpoint at `/ask` for querying.
- 🧱 **ChromaDB Integration**: High-performance vector storage.
- 🛠️ **Easy Setup**: Lightweight, readable architecture with minimal dependencies.

---

## 🧪 Sample Documents (Loaded at Startup)

```
- FastAPI is a modern web framework for building APIs with Python.
- ChromaDB is a vector database optimized for AI embeddings.
- FAISS enables efficient similarity search and clustering of dense vectors.
- OpenAI provides APIs for embedding, completion, and other AI services.
- Retrieval-Augmented Generation (RAG) enhances AI with contextual documents.
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API Key

In `core/config.py`, replace:

```python
OPENAI_API_KEY = "your-openai-api-key"
```

### 3. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Visit your API docs at:  
`http://localhost:8000/docs`

---

## 📦 API Endpoint

### `POST /ask`

#### Request

```json
{
  "query": "What is FastAPI?"
}
```

#### Response

```json
{
  "response": "FastAPI is a modern web framework for building APIs with Python."
}
```

---

## 📚 Tech Stack

- **FastAPI** — for building the web API
- **OpenAI** — for embeddings and completions
- **ChromaDB** — vector database for document storage
- **FAISS** — efficient similarity search
- **NumPy** — numerical computations

---

## 🧠 Future Improvements

- ✅ Add document upload interface  
- ✅ Integrate long-term memory storage  
- 🚧 Implement user authentication  
- 🚧 Add UI with query history

---

## 📄 License

This project is licensed under the MIT License.

---

