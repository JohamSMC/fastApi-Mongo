from fastapi import Query
from pydantic import BaseModel
from .tipoEjercicio import TipoEjercicio


class Ejercicio(BaseModel):
    id_ejercicio: int = Query(ge=1)
    tipo_ejercicio: TipoEjercicio
    nombre_ejercicio: str = Query(max_length=50)
    dsc_ejercicio: str = Query(max_length=200)
