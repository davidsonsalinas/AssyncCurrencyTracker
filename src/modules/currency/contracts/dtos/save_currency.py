from datetime import datetime
from pydantic import BaseModel, Field

class save_currency(BaseModel):
    currency: str = Field(..., title="Currency", description="Currency code")

