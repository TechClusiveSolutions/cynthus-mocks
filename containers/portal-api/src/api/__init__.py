"""Portal API initialization script for the Cynthus project"""

import logging

from fastapi import FastAPI

from api.routes import system


def initialize():
    logger = logging.getLogger(__name__)
    application = FastAPI()

    logger.debug('Configuring Portal application')

    application.include_router(system)

    return application


app = initialize()
