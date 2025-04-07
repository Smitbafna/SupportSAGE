# api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.assistant import generate_response

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask")
def ask(query_req: QueryRequest):
    answer = generate_response(query_req.query)
    return {"response": answer}
