from fastapi import APIRouter
from controllers import authors_controller
from models.author_model import AuthorCreate

router = APIRouter()

## aqui estoy siempre dependiendo de /autores
#/autores obtener una lista de todos los usuarios
@router.get('/', status_code=200)
async def get_all_authors():
    return await authors_controller.get_all()

#/autores/12 obtener un autor por id
@router.get('/{id_autor}', status_code=200)
async def get_authors_by_id(id_autor:str):
    return await authors_controller.get_by_id(int(id_autor))

#/autores enviar un autor nuevo empezamos a hablar de modelos.
@router.post('/', status_code=200)
async def create_author(autor:AuthorCreate):
    return await authors_controller.create(autor)