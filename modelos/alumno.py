#----------------------------Clase Alumno----------------------------------------------->
from .persona import Persona #.persona hace referencia al modulo actual

class Alumnos(Persona): #Alumno hereda de Persona

    def __init__(self, nombre, apellido, edad, asignatura):
        super().__init__(nombre, apellido, edad)
        self.asignatura=asignatura

    def __str__(self):
        return super().__str__() + " Asignatura: " + self.asignatura
