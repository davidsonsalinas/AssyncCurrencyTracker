from fastapi.encoders import jsonable_encoder

from src.modules.currency.contracts.dtos.save_currency import (
    save_currency,
)
from src.modules.currency.entities.currency import currency
from src.modules.currency.services.currency_respository.service import (
    CreateCurrencyService,
)
from src.providers.container import container


class CreateCurrencyEndpointController:
    @staticmethod
    async def handle(data: save_currency) -> currency:
        currency_repository_service = container.get(CreateCurrencyService)
        response = await currency_repository_service.execute(data)
        return jsonable_encoder(
            response.model_dump(by_alias=False, exclude={"revision_id"})
        )
