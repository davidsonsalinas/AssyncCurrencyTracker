from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.modules.currency.contracts.dtos.save_currency import (
    save_currency,
)

from src.modules.currency.entities.currency import currency

from src.modules.currency.services.currency_respository.controller import (
    CreateCurrencyEndpointController,
)


currency_endpoint_router = APIRouter(
    prefix="/currency_endpoint",
    tags=["currency_endpoint"],
)


@currency_endpoint_router.post("/post/", response_model=currency)  # type: ignore
async def create_currency_endpoint(data: save_currency) -> JSONResponse:
    response = await CreateCurrencyEndpointController.handle(data=data)
    return JSONResponse(response)
