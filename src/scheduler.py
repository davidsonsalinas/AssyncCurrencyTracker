from concurrent import futures
from arq import cron
from arq.connections import RedisSettings
from beanie import init_beanie
from src.jobs.controllers.insert_new_value import insert_new_value
from src.jobs.daily_currency import daily_currency

from motor.motor_asyncio import AsyncIOMotorClient

from typing import Any

from src.config.config import DOCUMENT_MODELS, MONGODB_URL

from src.config.redis_config import redis_config


async def startup(ctx: Any) -> str:
    scheduler_database = AsyncIOMotorClient(MONGODB_URL).arq
    # type: ignore
    await init_beanie(scheduler_database, document_models=DOCUMENT_MODELS)
    ctx["pool"] = futures.ProcessPoolExecutor()

    return "scheduler started"


async def shutdown(ctx: Any) -> str:

    return "scheduler shutdown"


class schedulerSettings:
    functions = [insert_new_value]  # type: ignore
    redis_settings = RedisSettings(
        redis_config.host,
        redis_config.port,
        password=redis_config.password,
        ssl=redis_config.ssl,
    )
    job_timeout = 42000
    retry_jobs = True
    max_tries = 5

    cron_jobs = [cron(daily_currency, minute=None, keep_result=1800)]  # type: ignore

    on_startup = startup
    on_shutdown = shutdown
