from fastapi import FastAPI
from routes.ejercicio import ejercicio
from routes.util import util
from docs import tags_metadata

app = FastAPI(
  title="FastAPI & Mongo CRUD",
  description="API para CRUD modulo 4 especialiazación BD Autores: Joham Medina, Miguel Sosa",
  version="1.0",
  openapi_tags=tags_metadata
)

app.include_router(ejercicio)
app.include_router(util)


