from fastapi import APIRouter

from app.api.v1.endpoints import *

api_v1_router = APIRouter()

@api_v1_router.get("/test")
def test():
    return {'test': 'test'}
