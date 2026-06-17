def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print('Error: no se puede dividir por cero')
    else:
        print(resultado)
    finally:
        print('ocurre siempre')


    
dividir(10, 5)

print('mas cosas')