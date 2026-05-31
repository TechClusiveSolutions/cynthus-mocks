"""Portal API System routes for the Cynthus project"""

import logging

from fastapi import APIRouter

system = APIRouter()


@system.get('/')
async def get_index():
    return {}
