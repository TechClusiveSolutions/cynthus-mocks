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


@event.subscriber('user.password.saved')
async def handle_user_password_saved_event(data: dict):
    logger = logging.getLogger(__name__)
    event = None

    logger.info('Received a user password saved event')
