# se conectara a bbdd
from db.config import get_conexion
import aiomysql as aio
from fastapi import HTTPException
from models.author_model import AuthorCreate

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
            return { "msg": 'Producto insertado correctamente', 'item': autor }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()
    