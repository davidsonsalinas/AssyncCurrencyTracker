import os

from typing import Any

from dotenv import load_dotenv

from src.jobs.contracts.implementations.beanie.document import currencyDaily


load_dotenv()


DOCUMENT_MODELS: list[Any] = [currencyDaily]


MONGODB_URL = os.getenv("MONGODB_URL") or ""
