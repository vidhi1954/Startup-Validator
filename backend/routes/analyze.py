import json
import logging

from fastapi import APIRouter, Depends, HTTPException

from database.db import SessionLocal
from database.models import Analysis
from graph.workflow import graph
from models.request import StartupRequest
from services.auth_services import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/analyze")
async def analyze(request: StartupRequest, current_user = Depends(get_current_user)):

    if not request.idea:
        raise HTTPException(status_code=400, detail="Idea is required")
    if len(request.idea)>2000:
        raise HTTPException(status_code=400, detail="Idea is too long. Maximum length is 2000 characters.")
    
    logger.info(f"Received request from user: {current_user.id}")

    try:
        result=await graph.ainvoke({"idea": request.idea})
        logger.info(f"Analysis result: {result}")

        # save to db
        db=SessionLocal()
        try:
            analysis=Analysis(
                user_id=current_user.id,
                idea=request.idea,
                result=json.dumps(result)
            )
            db.add(analysis)
            db.commit()
            db.refresh(analysis)
        finally:
            db.close()
        return {"result": result}
    except Exception as e:
        logger.error(f"Graph didn't invoke: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error : Graph didn't invoke")