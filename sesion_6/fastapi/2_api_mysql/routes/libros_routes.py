from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from controllers import libros_controller
from db.database_orm import get_db
from models.libro_orm import LibroCreate

router = APIRouter()

# obtener listado de libros
@router.get('/', status_code=200)
async def get_all_books(db: AsyncSession = Depends(get_db)):
    return await libros_controller.get_all(db)


# Crear un libro con ORM
@router.post('/', status_code=200)
async def create_libro(libro: LibroCreate, db: AsyncSession = Depends(get_db)):
    return await libros_controller.create(db, libro)