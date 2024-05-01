from src.jobs.enqueue_jobs import enqueue_jobs
from src.jobs.get_currency import get_currency


async def daily_currency(ctx) -> str:
    coins = ["USD", "GBP", "JPY", "AUD", "CAD", "EUR"]

    for coin in coins:
        currency = await get_currency(coin)
        await enqueue_jobs("insert_new_value", ctx=ctx, currency=coin, value=currency)

    return "All currencies updated!"
