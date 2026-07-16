def aviso_con_arguments(fn):
    def envoltura(*args, **kwargs):
        print('Inicio .....')
        print(fn(*args, **kwargs))
        print('Fin .....')
    return envoltura
        



@aviso_con_arguments
def restar(a, b):
    return a - b


restar(4, 6)
