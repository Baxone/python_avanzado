from fastapi import APIRouter
from controllers import authors_controller
from models.author_model import AuthorCreate, Author

router = APIRouter()

## aqui estoy siempre dependiendo de /autores
#/autores obtener una lista de todos los usuarios
#/autores?nacionalidad=colombiana
@router.get('/', status_code=200)
async def get_all_authors(nacionalidad:str = None):
    if nacionalidad:
        return await authors_controller.get_by_country(nacionalidad)
    else:
        return await authors_controller.get_all()

#/autores/12 obtener un autor por id
@router.get('/{id_autor}', status_code=200)
async def get_authors_by_id(id_autor:str):
    return await authors_controller.get_by_id(int(id_autor))

#/autores enviar un autor nuevo empezamos a hablar de modelos.
@router.post('/', status_code=200)
async def create_author(autor:AuthorCreate):
    return await authors_controller.create(autor)

#Borrar un autor por id
@router.delete('/{id_autor}', status_code=200)
async def delete_author_by_id(id_autor:str):
    return await authors_controller.delete_by_id(int(id_autor))

# Actualizar el autor por id (put, patch)
# put pasamos todo recurso, todo el autor
@router.put('/{id_autor}', status_code=200)
async def update_author_by_id(id_autor:str, autor:Author):
    return await authors_controller.update_by_id(int(id_autor), autor)

