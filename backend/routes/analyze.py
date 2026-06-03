from fastapi import APIRouter

from models.request import StartupRequest

from graph.workflow import graph

router = APIRouter()

@router.post("/analyze")
def analyze(request: StartupRequest):

    print("Received request:")

    initial_state = {
        "idea": request.idea
    }
    
    print("\n=== GRAPH START ===")
    
    result = graph.invoke(
        initial_state
    )
    print("\n=== GRAPH END ===")
    return result