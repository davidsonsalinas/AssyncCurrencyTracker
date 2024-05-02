from injector import Module, provider, singleton


from src.modules.currency.contracts.repositories.currency_repository import ( CurrencyRepository,)
from src.modules.currency.implementations.beanie.currency_endpoint import (  BeanieCurrencyRepository,)

class CurrencyRepositoryModule(Module):
    @singleton
    @provider
    def provide_currency_repository(self) -> CurrencyRepository:
        return BeanieCurrencyRepository()