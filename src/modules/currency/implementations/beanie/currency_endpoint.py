from src.modules.currency.contracts.dtos.save_currency import (
    save_currency,
)

from src.modules.currency.contracts.repositories.currency_repository import (
    CurrencyRepository,
)
from src.modules.currency.entities.currency import currency
from src.modules.currency.implementations.beanie.documents import (
    currencyEndpoint,
)


class BeanieCurrencyRepository(CurrencyRepository):
    
    async def create(self, data: save_currency) -> currency:  # type: ignore
        currency_endpoint = currencyEndpoint(**data.model_dump())  # type: ignore
        response = await currency_endpoint.insert()
        return response
