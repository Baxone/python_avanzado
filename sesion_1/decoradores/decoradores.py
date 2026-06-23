# funciones que aumentan la funcionalidad de otra funciones.

def sumar(a,b):
    return (a+b)

    
    
def restar(a,b):
   return (a-b)

    
def decoradora(fn, n1, n2):
    resultado = fn(n1,n2)
    print(resultado)
    
decoradora(restar, 1, 2)