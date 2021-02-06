from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from app.core.config import settings
from app.api.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_STR)



