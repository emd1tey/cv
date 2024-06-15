import logging
from fastapi import APIRouter, HTTPException

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/api/error_404")
async def error_404():
    logger.error("404 Not Found error triggered")
    raise HTTPException(status_code=404, detail="Resource not found")


@router.get("/api/error_500")
async def error_500():
    logger.error("500 Internal Server Error triggered")
    raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/api/division_by_zero")
async def division_by_zero():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("Division by zero error")
        raise HTTPException(status_code=500, detail="Division by zero error")
    return {"result": result}


@router.get("/api/value_error")
async def value_error():
    try:
        raise ValueError("This is a value error")
    except ValueError:
        logger.exception("Value error triggered")
        raise HTTPException(status_code=400, detail="Value error occurred")


@router.get("/api/success")
async def success():
    logger.info("Success endpoint accessed")
    return {"message": "This endpoint works correctly"}


@router.get("/api/slow")
async def slow():
    import time
    logger.info("Slow endpoint accessed, simulating delay")
    time.sleep(5)
    return {"message": "This was a slow response"}


@router.get("/api/custom")
async def custom_exception():
    try:
        raise Exception("This is a custom exception for testing")
    except Exception:
        logger.exception("Custom exception triggered")
        raise HTTPException(status_code=500, detail="Custom exception occurred")
