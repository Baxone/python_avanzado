def aviso(fn, titulo, prioridad):
    def envoltura():
        print('Iniciando tarea...')
        print(fn(titulo, prioridad))
        print('Terminando tarea...')
    return envoltura

def tarea(titulo, prioridad):
    if prioridad == 1:
        return f"La tarea {titulo} es urgente"
    elif prioridad == 2:
        return f"La tarea {titulo} es diaria"
    elif prioridad == 3:
        return f"La tarea {titulo} es mensual"
    
print( tarea('Estudiar python', 1) )

tarea_con_aviso = aviso(tarea, 'estudiar python', 1)
print( tarea_con_aviso() )