from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from models.libro_orm import LibroORM, Libro, LibroCreate

async def get_all(db: AsyncSession):
    try:
        result = await db.execute(select(LibroORM))
        # scalars() extrae solo los objetos LibroORM del resultado de la consulta,
        # y all() los devuelve todos juntos en una lista.
        libros = result.scalars().all()
        libros_final = []
        for libro in libros:
            libros_final.append(Libro.model_validate(libro))
        return { 'cantidad': len(libros_final), 'result': libros_final }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    
    
async def create(db: AsyncSession, libro: LibroCreate):
    try:
        nuevo_libro = LibroORM(
            titulo=libro.titulo,
            isbn=libro.isbn,
            anio_publicacion=libro.anio_publicacion,
            id_autor=libro.id_autor
        )
        db.add(nuevo_libro)
        await db.commit()
        await db.refresh(nuevo_libro)
        print(nuevo_libro)
        return {'msg': 'Libro creado correctamente', 'libro': Libro.model_validate(nuevo_libro)}
        
    except IntegrityError:
          # rollback() deshace los cambios pendientes de la transacción para evitar guardar datos inválidos.
          await db.rollback()
          raise HTTPException(status_code=400, detail='El autor indicado no existe o el ISBN ya está en uso')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')