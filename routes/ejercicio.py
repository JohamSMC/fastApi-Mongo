from typing import List
from pymongo import ReturnDocument
from fastapi import APIRouter, status, Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND

from models.ejercicio import Ejercicio
from config.db import conn
from config.contants import TAG_EJERCICIOS


ejercicio = APIRouter()


@ejercicio.get('/ejercicios', response_model=List[Ejercicio], tags=[TAG_EJERCICIOS])
async def find_all_ejercicios():
    # print(list(conn.local.ejercicio.find()))
    return list(conn.local.ejercicio.find())


@ejercicio.post('/ejercicios', response_model=Ejercicio, tags=[TAG_EJERCICIOS])
async def create_ejercicio(ejercicio: Ejercicio):
    ejercicio.tipo_ejercicio = dict(ejercicio.tipo_ejercicio)
    new_ejercicio = dict(ejercicio)
    if conn.local.ejercicio.find_one({"id_ejercicio": ejercicio.id_ejercicio}):
        return Response(status_code=HTTP_409_CONFLICT)
    id_ejercicio = conn.local.ejercicio.insert_one(new_ejercicio).inserted_id
    ejercicio = conn.local.ejercicio.find_one({"_id": id_ejercicio})
    return ejercicio


@ejercicio.get('/ejercicios/{id}', response_model=Ejercicio, tags=[TAG_EJERCICIOS])
async def find_ejercicio(id: int):
    ejercicio = conn.local.ejercicio.find_one({"id_ejercicio": id})
    print(ejercicio)
    if ejercicio:
        return ejercicio
    return Response(status_code=HTTP_404_NOT_FOUND)


@ejercicio.put("/ejercicios/{id}", response_model=Ejercicio, tags=[TAG_EJERCICIOS])
async def update_ejercicio(id: int, ejercicio: Ejercicio):
    validate_id = conn.local.ejercicio.find_one(
        {"id_ejercicio": id})

    if validate_id:
        ejercicio.tipo_ejercicio = dict(ejercicio.tipo_ejercicio)
        update_ejercicio = conn.local.ejercicio.find_one_and_update({
            "id_ejercicio": id
        }, {
            "$set": dict(ejercicio)
        }, return_document = ReturnDocument.AFTER)
        return update_ejercicio
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


@ejercicio.delete("/ejercicios/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=[TAG_EJERCICIOS])
async def delete_ejercicio(id: int):
    delete_ejercicio = conn.local.ejercicio.find_one_and_delete(
        {"id_ejercicio": id})
    if delete_ejercicio:
        return Response(status_code=HTTP_204_NO_CONTENT)
    return Response(status_code=HTTP_404_NOT_FOUND)
