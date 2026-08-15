from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger_config import logger
from fastapi.exceptions import RequestValidationError
from .app_exception import AppException



async def app_exception_handler(
    request: Request,
    exc: AppException
):
    logger.warning(
        "Application error | %s | %s",
        request.url.path,
        exc.message)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.error_code,
                "message": exc.message
            }
        }
    )

async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        "Unhandled exception | %s",
        request.url.path)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Something went wrong"
            }
        }
    )

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(location) for location in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": error
            }
        }
    )



