from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# INPUT MODEL
class RecommendationRequest(BaseModel):
    reservationId: str

# API ENDPOINT
@app.post("/agent/recommendations")
def get_recommendation(request: RecommendationRequest):

    # MOCK AGENT RESPONSE
    return {
        "recommendations": [
            {
                "label": "Upgrade to Toyota Fortuner",
                "action": "ASSIGN_VEHICLE",
                "reason": "Gold customer prefers SUV"
            },
            {
                "label": "Offer premium insurance",
                "action": "ADD_INSURANCE"
            }
        ]
    }