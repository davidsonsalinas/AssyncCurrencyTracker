from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class currency(BaseModel):
    currency: str
