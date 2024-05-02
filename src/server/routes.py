from typing import Any

from fastapi.routing import APIRouter

from src.modules.currency.routers.currency_endpoint import currency_endpoint_router


router = APIRouter()

router.include_router(currency_endpoint_router)
