import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

# reutilizamos aiomysql para atraves de SQLAlchemy (mysql+aiomysql)
# Ejemplo sin variables de entorno:
# mysql+aiomysql://usuario:password@localhost:8889/mi_base_de_datos
DATABASE_URL = (
    f"mysql+aiomysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}:{os.getenv("MYSQL_PORT")}/{os.getenv("MYSQL_DB")}"
)

# Crea el motor asíncrono de SQLAlchemy usando la URL de conexión a MySQL;
# es el objeto encargado de gestionar conexiones con la base de datos.
engine = create_async_engine(DATABASE_URL, echo=False)

# Crea una fábrica de sesiones asíncronas (una nueva sesión por uso),
# enlazada al motor y sin expirar objetos tras cada commit.
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# para poder generar modelos ORM 
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session