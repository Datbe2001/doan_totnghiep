from fastapi import APIRouter

from app.api.endpoint import user
from app.api.endpoint import course
from app.api.endpoint import lesson
from app.api.endpoint import comment

route = APIRouter()

route.include_router(user.router, tags=["users"])
route.include_router(course.router, tags=["courses"])
route.include_router(lesson.router, tags=["lessons"])
route.include_router(comment.router, tags=["comments"])
