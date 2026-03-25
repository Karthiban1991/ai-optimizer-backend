from fastapi import APIRouter
from app.services.k8s_service import K8sService
from app.services.ai_agent import AIAgent

router = APIRouter()

k8s = K8sService()
ai = AIAgent()

@router.get("/pods")
def get_pods():
    return k8s.list_pods()

@router.post("/chat")
def chat(prompt: str):
    return {"response": ai.run(prompt)}
