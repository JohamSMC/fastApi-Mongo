from operator import ge
from fastapi import Query
from pydantic import BaseModel
from typing import Optional


class TipoEjercicio(BaseModel):
    id_tipo_ejercicio: int = Query(ge=1)
    dsc_tipo_ejercicio: str = Query(max_length=50)
    dificulta_ejercicio: Optional[int] = Query(ge=0, lt=50)
