import pickle
import asyncio
import logging
import aiomcache

from .config import Config

loop = asyncio.get_event_loop()
log = logging.getLogger('application')

try:
    from io import BytesIO
except ImportError:
    from io import StringIO as BytesIO


class Cache:
    mc = aiomcache.Client(host=Config.get('cache', 'host'), port=Config.get('cache', 'port'), loop=loop)

    @classmethod
    async def set(cls, key, value, expired_time=0):
        key = str(key).encode()
        value = pickle.dumps(value)
        res = await cls.mc.set(key, value, exptime=expired_time)
        if not res:
            log.exception("Error setting cache")

    @classmethod
    async def add(cls, key, value, expired_time=0):
        key = str(key).encode()
        value = pickle.dumps(value)
        res = await cls.mc.add(key, value, expired_time)
        return res

    @classmethod
    async def delete(cls, key):
        key = str(key).encode()
        res = await cls.mc.delete(key)
        if not res:
            log.exception("Error deleting cache")

    @classmethod
    async def get(cls, key):
        key = str(key).encode()
        res = await cls.mc.get(key)
        if res:
            res = pickle.loads(res)
        return res
