"""Chat System routes for the Cynthus project"""


from fastapi import APIRouter

system = APIRouter()


@system.get('/')
async def get_index():
    return {}
