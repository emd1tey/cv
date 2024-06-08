# src/routes/cv.py
from fastapi import APIRouter, HTTPException
from src.utils.cv_generator import create_cv
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/api/cv")
async def generate_cv():
    try:
        await create_cv()
        return {"message": "CV generated successfully"}
    except Exception as e:
        logger.error(f"Error generating CV: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
