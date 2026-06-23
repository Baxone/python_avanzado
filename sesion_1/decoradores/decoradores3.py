def aviso(fn):
    def envoltura():
        print('Iniciando tarea...')
        print(fn())
        print('Terminando tarea...')
    return envoltura


@aviso
def tarea():
        return "La tarea es urgente"
    
    
@aviso
def saludar():
    return 'Hola como estan los maquinas'
    

tarea()
saludar()
    


