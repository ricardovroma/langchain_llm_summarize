from logging import Logger

from src.config import settings

logging = Logger(name=settings["APP_NAME"], level=settings["LOG_LEVEL"])
