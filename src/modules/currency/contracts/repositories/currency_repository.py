from abc import ABC, abstractmethod

from src.modules.currency.contracts.dtos.save_currency import (
    save_currency,
)

from src.modules.currency.entities.currency import currency


class CurrencyRepository(ABC):
    @abstractmethod
    async def create(self, data: save_currency) -> currency:
        raise Exception("Not implemented")
