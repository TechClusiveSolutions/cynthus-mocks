"""Event routes for the Cynthus project"""

import logging

from os import environ

from faststream.redis.fastapi import RedisRouter


host = environ.get('CACHE_HOST')
port = environ.get('CACHE_PORT')
username = environ.get('CACHE_USERNAME')
password = environ.get('CACHE_PASSWORD')
url = f'redis://{username}:{password}@{host}:{port}/0'
event = RedisRouter(url)


@event.subscriber('suggestion.accepted')
async def handle_suggestion_accepted_event(data: dict):
    logger = logging.getLogger(__name__)
    event = None

    logger.info('Received a suggestion accepted event')
