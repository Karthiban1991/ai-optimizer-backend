from fastapi import APIRouter
from app.services.k8s_service import K8sService
from app.services.ai_engine import AIEngine
from app.services.cost_engine import CostEngine
from app.services.rl_agent import RLAgent

router = APIRouter()

k8s = K8sService()
ai = AIEngine()
cost = CostEngine()
rl = RLAgent()

@router.get("/pods")
def pods():
    return k8s.list_pods()

@router.get("/cost")
def get_cost():
    pods = k8s.list_pods()
    return cost.calculate_cluster(pods)

@router.post("/optimize")
def optimize():
    pods = k8s.list_pods()
    return ai.optimize(pods)

@router.post("/chat")
def chat(data: dict):
    return {"response": "AI processed: " + data["prompt"]}
