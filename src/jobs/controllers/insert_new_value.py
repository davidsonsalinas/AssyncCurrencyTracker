from typing import Any


from src.jobs.contracts.implementations.beanie.document import currencyDaily


async def insert_new_value(
    ctx: Any, currency: str, value: int) -> Any:

    dolar = currencyDaily(  
        name=currency,
        price=value,
    )
    await dolar.save()
    return dolar
