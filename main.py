from fastapi import FastAPI
from schemas import RecommendRequest, RecommendResponse
from model import recommend

app = FastAPI(title="Course Recommendation Service")

@app.post("/recommend", response_model=RecommendResponse)
def recommend_api(req: RecommendRequest):
    if not req.data:
        return RecommendResponse(userId=-1, items=[])

    recommendations = recommend(
        data=req.data,
        target_user_id=req.targetUserId,
        top_n=req.topN
    )

    return RecommendResponse(
        userId=req.targetUserId,
        items=recommendations
    )