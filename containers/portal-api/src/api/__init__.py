"""Portal API initialization script for the Cynthus project"""

import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
from os import environ
from redis import asyncio as aioredis

from api.routes import event, system


@asynccontextmanager
async def lifespan(application: FastAPI):
    host = environ.get('CACHE_HOST')
    port = environ.get('CACHE_PORT')
    username = environ.get('CACHE_USERNAME')
    password = environ.get('CACHE_PASSWORD')
    url = f'redis://{username}:{password}@{host}:{port}/0'
    client = aioredis.from_url(url)

    # Startup: Initialize Redis pool
    application.state.redis = client

    yield

    # Shutdown: Close Redis pool
    await application.state.redis.close()


def initialize():
    logger = logging.getLogger(__name__)
    application = FastAPI(lifespan=lifespan)

    logger.debug('Configuring Portal application')

    application.include_router(event)
    application.include_router(system)

    return application


app = initialize()
