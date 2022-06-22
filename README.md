# FastAPI Mongodb REST API

* Joham Sebastian Medina Corredor  [![Git-JohamSMC](https://img.shields.io/badge/GitHub-JohamSMC-red?style=plastic&logo=github&link=https://github.com/JohamSMC)](https://github.com/JohamSMC)
* Miguel Angel Sosa

### RESOURCES
* https://fastapi.tiangolo.com/
* https://fastapi.tiangolo.com/tutorial/response-model/


### 1 paso:
> Se sugiere crear un entorno virtual, para lo cual se debe tener instalado ***python*** y el gestor de paquetes ***PIP***

### 2 paso:
> Crear entorno virtual con  **venv**

```
python -m venv env
o
python3 -m venv env
```

### 3 paso:
> Activar  **venv**

* Linux
```
source env/bin/activate
```
* Windows
```
env\Scripts\activate
```

### 4 paso:
> Nos ubicamos en la carpeta raiz del proyecto y verificamos que existe el archivo
***``requirements.txt``***

> y ejecutamos el comando:

```
pip install -r requirements.txt
```

> Con este comando se instalara todas las librerias necesarias para el proyecto.

### 5 paso:
> Despues procedemos a correr el proyecto en modo desarrollo ("Estando Ubicados en la raiz del proyecto") con el comando:

```
uvicorn main:app --reload
```