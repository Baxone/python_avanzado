# importar la libreria fast api
from fastapi import FastAPI

# arrancar el servidor 
app = FastAPI()

@app.get("/")
def root():
    return "Hola desde fast api"


@app.get("/mi_nombre")
def get_name():
    return "Hola me llamo Juan Antonio"


@app.delete("/borrado")
def borrado():
    return "acabas de eliminarme"