from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime
from db.database_orm import Base

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


class AuthorORM(Base):
    __tablename__ = 'autores'

    id_autor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150), nullable=False)
    nacionalidad = Column(String(80), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=True)