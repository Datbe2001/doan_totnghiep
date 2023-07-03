from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.depend import oauth2
from app.utils.response import make_response_object

from ...schemas import LessonCreateParams, LessonUpdate
from ...model.base import CourseType
from ...model import User
from ...services import LessonService


router = APIRouter()

@router.get("/lesson/list")
async def list_lesson(user: User = Depends(oauth2.get_current_user),
                      db: Session = Depends(get_db),
                      skip=0,
                      limit=10):
    lesson_service = LessonService(db=db)

    lesson_response = await lesson_service.list_lesson(skip=skip, limit=limit)
    return make_response_object(lesson_response)


@router.get("/lesson/{lesson_id}")
async def get_lesson_by_id(lesson_id: str, 
                            user: User = Depends(oauth2.get_current_user),
                            db: Session = Depends(get_db)):
    
    lesson_service = LessonService(db=db)

    lesson_response = await lesson_service.get_lesson_by_id(lesson_id=lesson_id)
    return make_response_object(lesson_response)


@router.post("/lesson/create")
async def create_lesson(lesson_create: LessonCreateParams,
                        user: User = Depends(oauth2.user_manager),
                        db: Session = Depends(get_db)):
    
    lesson_service = LessonService(db=db)

    lesson_response = await lesson_service.create_lesson(lesson_create=lesson_create)
    db.refresh(lesson_response)
    return make_response_object(lesson_response)


@router.put("/lesson/update/{lesson_id}")
async def update_lesson(lesson_id: str,
                        lesson_update: LessonUpdate,
                        user: User = Depends(oauth2.user_manager),
                        db: Session = Depends(get_db)):
    
    lesson_service = LessonService(db=db)

    lesson_response = await lesson_service.update_lesson(lesson_id=lesson_id,
                                                         lesson_update=lesson_update)
    return make_response_object(lesson_response)


@router.delete("/lesson/delete/{lesson_id}")
async def delete_lesson(lesson_id: str,
                        user: User = Depends(oauth2.user_manager),
                        db: Session = Depends(get_db)):
    
    lesson_service = LessonService(db=db)

    lesson_response = await lesson_service.delete_lesson(lesson_id=lesson_id)
    return make_response_object(lesson_response)
