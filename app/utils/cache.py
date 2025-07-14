
from typing import Optional, Callable, Any, Dict

import redis.asyncio as redis

import asyncio

import os

import json

import logging


REDIS_HOST = os.getenv("REDIS_URL", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)

redis_clients : Dict[int, redis.Redis] = {}

logger = logging.getLogger(__name__)

NO_REDIS_CLIENT_ERROR = "Redis client is not initialized. Please check your Redis configuration."
REDIS_TTL = int(os.getenv("CACHE_TTL", 600))  # Default TTL for cache in seconds



def check_redis_client(func : Callable):
    """
    Checks if the Redis client is initialized.
    Raises:
        RuntimeError: If the Redis client is not initialized.
    """
    async def wrapper(*args, **kwargs):
        loop_id = id(asyncio.get_running_loop())
        if loop_id not in redis_clients:
            try:
                redis_clients[loop_id] = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
            except (ConnectionError, TimeoutError) as e:
                logger.error(f"{NO_REDIS_CLIENT_ERROR}: {e}")
                raise RuntimeError(NO_REDIS_CLIENT_ERROR)
        return await func(redis_clients[loop_id], *args, **kwargs)
    return wrapper


@check_redis_client
async def set_cache(redis_client : redis.Redis, key: str, value: Any, ttl: int = REDIS_TTL) -> None:
    """
    Sets a value in the Redis cache with an optional TTL.
    Args:
        key (str): The key for the cached value.
        value (str): The value to cache.
        ttl (int): Time to live in seconds. Default is 60 seconds.
    """

    await redis_client.set(key, json.dumps(value), ex=ttl)
    logger.info(f"Set cache for key: {key} with TTL: {ttl} seconds")


@check_redis_client
async def get_cache(redis_client : redis.Redis, key: str) -> Optional[str]:
    """
    Retrieves a value from the Redis cache.
    Args:
        key (str): The key for the cached value.
    Returns:
        str: The cached value or None if not found.
    """

    data = await redis_client.get(key)
    return json.loads(data) if data else None


@check_redis_client
async def is_in_cache(redis_client : redis.Redis, key: str) -> bool:
    """
    Checks if a key exists in the Redis cache.
    Args:
        key (str): The key to check.
    Returns:
        bool: True if the key exists, False otherwise.
    """

    exists = await redis_client.exists(key)
    return exists



@check_redis_client
async def flush_cache(redis_client: redis.Redis) -> None:
    """
        Delete all keys in the Redis database.
        Args:
            r (redis.Redis): The Redis client instance.
        Returns:
            None
    """

    await redis_client.flushdb()