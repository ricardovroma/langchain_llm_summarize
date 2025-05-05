from fastapi import APIRouter

from src.router import healthcheck, llm


def setup_router():
    router = APIRouter()
    router.include_router(healthcheck.setup(), prefix="", tags=["Health Check"])
    router.include_router(llm.router, prefix="", tags=["Disclose/Deidentify"])
    return router
