from sqlalchemy import Column, Integer, String, ForeignKey
from db.database_orm import Base
from pydantic import BaseModel, ConfigDict

class LibroCreate(BaseModel):
    titulo: str
    isbn: str
    anio_publicacion: int
    id_autor: int



class Libro(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id_libro:int
    titulo: str
    isbn: str
    anio_publicacion: int
    id_autor: int

class LibroORM(Base):
    __tablename__ = 'libros'
    
    id_libro= Column(Integer, primary_key=True, autoincrement=True)
    titulo=Column(String(150), nullable=False)
    isbn=Column(String(20), unique=True, nullable=True)
    anio_publicacion = Column(Integer, nullable=True)
    id_autor= Column(Integer, ForeignKey('autores.id_autor'), nullable=False)