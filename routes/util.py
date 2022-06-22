from asyncio.windows_events import NULL
from typing import List
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import APIRouter, status, Response

from config.db import conn
from config.contants import TAG_UTIL
from models.ejercicio import Ejercicio


util = APIRouter()


@util.get('/custom-query', response_model=List[Ejercicio], tags=[TAG_UTIL])
async def custom_query():
    return list(conn.local.ejercicio.find(filter={'tipo_ejercicio.dificulta_ejercicio': {'$ne': None}}))


@util.get('/custom-query2', response_model=List[Ejercicio], tags=[TAG_UTIL])
async def custom_query2():
    return list(conn.local.ejercicio.find(filter=({"$and": [{'tipo_ejercicio.dificulta_ejercicio': {'$ne': None}}, {'tipo_ejercicio.dificulta_ejercicio': {'$gte': 1}}]})))
