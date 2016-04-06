import sys

from modelos.alumno import Alumnos
from modelos.persona import Persona

#----------------------------Main-------------------------------------------------------->

#def consulta(numero=numero): si es esto significa que das un valor por defecto
def agregar(numero,bbdd=[]): #recibe el numero y la lista
 
    #Longitud de las personas
    for i in range(numero):
       
        #python2 utiliza raw_input lee nombre y idiomas
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))
        edad = int(input("Introduce numero de edad: "))
        asignatura = str(input("Introduce asignaturas: "))
        #Agrega las personas con las claves
        bbdd.append(Alumnos(nombre,apellido,edad,asignatura))

    return bbdd

def mostrar(bbdd):

    for i in bbdd:
        print(i)
      # print(persona.nombre) acceder a los atributos de una clase

def mostrar_adultos(bbdd):
    print("------>Estas son las personas mayores<-------")
    for i in bbdd:
        if i.mayor_de_edad():
            print(i)





bbdd = [
        Alumnos('luis','Garcia',23,'matematicas'),
        Alumnos('Daniel','Sanchez', 17,'ingles'),
        Alumnos('Maria','Gomez', 15,'fisica'),
        Alumnos('Luisa','Fernandez',21,'ingles')
]

#Numero de alumnos
while True:

	try:
	    numero = int(input("Introduce el numero de alumnos:"))
		break
	except ValueError:
	    print("Introduce un numero")
	    sys.exit()
#Llama a la funcion para agregar a las personas

bbdd = agregar(numero,bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)