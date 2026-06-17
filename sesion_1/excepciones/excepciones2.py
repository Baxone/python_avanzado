# yo puedo crear mi propio Error creando una clases
class MiError(Exception):
    pass

class ConexionError(Exception):
    pass

try:
    numero = int(input('Dime un numero: '))
    if numero < 0:
        raise MiError('El numero no puede ser negativo')
    print(numero)
except MiError as e:
    print(f'Error: {e}') 
except Exception:
    print('error generico') 
    



    

      