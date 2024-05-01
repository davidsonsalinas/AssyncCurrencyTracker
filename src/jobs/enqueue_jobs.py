from typing import Any, Dict, Optional
from arq import ArqRedis


async def enqueue_jobs(
    job_name: str, ctx: Optional[Dict[Any, Any]] = None, *args: Any, **kwargs: Any # noqa
) -> Any:
    if ctx is None:
        raise ValueError("Context is required to enqueue jobs")
    ctx_redis: ArqRedis = ctx["redis"]
    await ctx_redis.enqueue_job(
        job_name,
        *args,
        **kwargs,
    )
