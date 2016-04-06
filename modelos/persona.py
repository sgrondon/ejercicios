#---------------------------Clase Persona-------------------------------------------------->

class Persona():
    #this java funcion constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property #cambiar la funcion en atributo
    def mayor_de_edad(self): #siempre pasar el self
       return self.edad >= 18 #devolvera true o false 
        
    def __str__(self):#toString de java
        return self.nombre + " " + self.apellido + ", "+ str(self.edad)

