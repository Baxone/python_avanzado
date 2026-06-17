
class Usuario():
    nombre:str
    edad: int
    email: str
    password: str
    estado: bool
    
    
class Estudiante():
    # variables de clase
    __nombre:str
    edad: int
    email: str
    password: str
    estado: bool
    
    def __init__(self, nombre, edad, email):
        # variables de instancia
        self.__nombre = nombre
        self.edad = edad
        self.email = email
        self.estado = True
        self.password = "12456"
        
    
    # setter
    def actualizar_nombre(self, nombre):
        self.nombre = nombre
        
    # getter
    def mostrar_nombre(self):
        return self.__nombre
    
alumno = Estudiante('Ana', 20, 'ana@gmail.com')
print(alumno.mostrar_nombre())
    
    
        