
import requests

async def get_currency(currency: str) -> float:
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
    data = response.json()
    return data["rates"]["BRL"]