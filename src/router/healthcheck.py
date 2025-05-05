from fastapi import APIRouter
from fastapi.responses import Response
from starlette import status

from src.logger import logging


def setup():
    router = APIRouter()

    @router.get("/healthcheck")
    def healthcheck():
        logging.info("Healthy")
        return Response(
            status_code=status.HTTP_200_OK,
            content="Healthy")

    return router
