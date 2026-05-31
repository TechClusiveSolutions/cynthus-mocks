"""Chat initialization script for the Cynthus project"""

import logging

from fastapi import FastAPI

from chat.routes import system


def initialize():
    logger = logging.getLogger(__name__)
    application = FastAPI()

    logger.debug('Configuring Chat application')

    application.include_router(system)

    return application


app = initialize()
