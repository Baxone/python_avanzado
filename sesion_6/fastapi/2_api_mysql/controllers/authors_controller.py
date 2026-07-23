# se conectara a bbdd
from db.config import get_conexion
import aiomysql as aio
from fastapi import HTTPException
from models.author_model import AuthorCreate, Author
# importara la libreria para trabajar con mysql aiomysql

async def get_all():
    try:
        # obtener el acceso bbdd forma asincrona a traves de get_conexion
        conn = await get_conexion()
        # voy abrir sql para poder lanzar la peticion sql
        async with conn.cursor(aio.DictCursor) as cursor:
            # lanzamos la consulta a bbdd
            await cursor.execute('SELECT * FROM autores')
            # convertir las consultas sql en un lista de diccionarios
            results = await cursor.fetchall()
            return { 'cantidad_autores': len(results), 'ultimo_id': results[-1]['id_autor'], 'results': results }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        # ya se a por error o por acierto cierro la conexion a bbddd
        conn.close()
        
        
async def get_by_id(id_autor: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aio.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM autores WHERE id_autor=%s", (id_autor,))
            autor =await cursor.fetchone()
            return autor if autor else { 'msg': 'Autor no encontrado' }  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()
        

async def create(autor: AuthorCreate):
    # como norma deberiamos comprobar duplicados con alguna funcion get_by_email()
    try:
        conn = await get_conexion()
        async with conn.cursor(aio.DictCursor) as cursor:
            await cursor.execute('INSERT INTO autores (nombre, apellidos, nacionalidad, fecha_nacimiento) VALUES (%s,%s,%s,%s)', (autor.nombre, autor.apellidos, autor.nacionalidad, autor.fecha_nacimiento))
            await conn.commit()
            # insertrows, lastrowid, tengo que recuperar el id de nuevo usuario
            nuevo_id = cursor.lastrowid
            autor = await get_by_id(nuevo_id)
            return { "msg": 'Autor insertado correctamente', 'item': autor }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()


async def delete_by_id(id_autor: int):
    ## si existe el autor que vamos a borrar.
    autor = await get_by_id(id_autor)
    if isinstance(autor, dict) and 'msg' in autor:
        raise HTTPException(status_code=404, detail='El autor que intentas borrar no existe')
    # el autor existe y lo puedo borrar
    try:
        conn = await get_conexion()
        async with conn.cursor(aio.DictCursor) as cursor:
            await cursor.execute('DELETE FROM autores WHERE id_autor=%s', (id_autor,))
            await conn.commit()
            return { 'msg': f'Autor con id {id_autor} ha sido eliminado', 'autor_eliminado': autor  }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()
        
 
async def get_by_country(country: str):
    try:
        conn = await get_conexion()
        async with conn.cursor(aio.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM autores WHERE nacionalidad=%s", (country,))
            autor =await cursor.fetchall()
            return autor if autor else { 'msg': 'No existe ningun autor con esa nacionalidad' }  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close() 
 
       
async def update_by_id(id_autor: int, autor: Author):
    # comprobar que id_autor corresponde con el id autor
    if id_autor != autor.id_autor:
        raise HTTPException(status_code=400, detail="El ID del autor no coincide con el de la ruta")
    # autor existe
    autor_update = await get_by_id(id_autor)
    if isinstance(autor_update, dict) and 'msg' in autor_update:
        raise HTTPException(status_code=404, detail="El autor que intentas actualizar no existe")
    try:
        conn = await get_conexion()
        async with conn.cursor(aio.DictCursor) as cursor:
            await cursor.execute(
                "UPDATE autores SET nombre=%s, apellidos=%s,  nacionalidad=%s, fecha_nacimiento=%s WHERE id_autor=%s", (autor.nombre, autor.apellidos, autor.nacionalidad, autor.fecha_nacimiento, autor.id_autor)
            )
            await conn.commit()
            return {'msg': 'Autor actualizado correctamente', 'autor': await get_by_id(id_autor)}
    except Exception as e:
           raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()