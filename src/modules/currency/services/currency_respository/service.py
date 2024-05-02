from injector import inject

from src.modules.currency.contracts.dtos.save_currency import (
    save_currency,
)
from src.modules.currency.contracts.repositories.currency_repository import (
    CurrencyRepository,
)
from src.modules.currency.entities.currency import currency


class CreateCurrencyService:
    @inject
    def __init__(self, currency_repository: CurrencyRepository):
        self.currency_repository = currency_repository

    async def execute(self, data: save_currency) -> currency:
        currency = await self.currency_repository.create(data)
        return currency
