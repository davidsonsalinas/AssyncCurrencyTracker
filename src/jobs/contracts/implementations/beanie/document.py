from beanie import Document
from datetime import datetime


class currencyDaily(Document):
    class Settings:
        collection = "currencyDaily"
        name = "currencyDaily"

    name: str
    price: float
    date: datetime = datetime.now()

