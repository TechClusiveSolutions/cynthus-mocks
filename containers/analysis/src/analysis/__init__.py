"""Analysis initialization script for the Vesta project"""

import logging

from fastapi import FastAPI

from analysis.routes import system


def initialize():
    logger = logging.getLogger(__name__)
    application = FastAPI()

    logger.debug('Configuring API application')

    application.include_router(system)

    return application


app = initialize()
