# importar la libreria fast api
from fastapi import FastAPI
from routes import authors_routes

# arrancar el servidor 
app = FastAPI()


# inclusion de los ficheros de rutas
#autores
# http://localhost:8000/autores
app.include_router(authors_routes.router, prefix="/autores", tags=['Autores'])


# @app.get("/")
# def root():
#     return "Hola desde fast api"


# @app.get("/mi_nombre")
# def get_name():
#     return "Hola me llamo Juan Antonio"


# @app.delete("/borrado")
# def borrado():
#     return "acabas de eliminarme"