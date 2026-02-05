from pydantic import BaseModel
from typing import List

class UserCourseScore(BaseModel):
    userId: int
    courseId: int
    score: float

class RecommendRequest(BaseModel):
    targetUserId: int
    data: List[UserCourseScore]
    topN: int = 5

class CourseRecommendation(BaseModel):
    courseId: int
    score: float

class RecommendResponse(BaseModel):
    userId: int
    items: List[CourseRecommendation]