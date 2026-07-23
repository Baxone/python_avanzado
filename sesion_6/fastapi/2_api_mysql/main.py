# importar la libreria fast api
from fastapi import FastAPI
from routes import authors_routes, libros_routes
from models.author_model import AuthorORM
from models.libro_orm import LibroORM

# arrancar el servidor 
app = FastAPI()


# inclusion de los ficheros de rutas
#autores
# http://localhost:8000/autores
app.include_router(authors_routes.router, prefix="/autores", tags=['Autores'])
app.include_router(libros_routes.router, prefix="/libros", tags=['Libros'])


# @app.get("/")
# def root():
#     return "Hola desde fast api"


# @app.get("/mi_nombre")
# def get_name():
#     return "Hola me llamo Juan Antonio"


# @app.delete("/borrado")
# def borrado():
#     return "acabas de eliminarme"