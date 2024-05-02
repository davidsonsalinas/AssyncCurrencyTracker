from injector import Injector

from src.config.container_config import (
    CurrencyRepositoryModule,
)

container = Injector(
    [
        CurrencyRepositoryModule()
    ]
)
