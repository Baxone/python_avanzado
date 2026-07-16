from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Author(BaseModel):
    id_autor: int
    nombre: str
    apellidos: str
    nacionalidad: str
    fecha_nacimiento: Optional[datetime] = None
    
class AuthorCreate(BaseModel):
    nombre: str
    apellidos: str
    nacionalidad: str
    fecha_nacimiento: Optional[datetime] = None