# src/routes/cv.py
import logging

from fastapi import APIRouter, HTTPException

from src.utils.gendoc import create_cv

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
