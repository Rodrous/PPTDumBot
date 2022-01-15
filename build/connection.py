import os
from typing import Coroutine
import motor.motor_asyncio


async def connection() -> Coroutine:
    client: str = os.environ.get("mongoDb")
    cursor = motor.motor_asyncio.AsyncIOMotorClient(client)
    return cursor


def createdb(connectionobj, databasename, collectionname):
    db = connectionobj[databasename]
    collection = db[collectionname]
    return collection
