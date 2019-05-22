# usando mis modulos, primero hacemos el from de la carpeta y el archivo y luego el import de los metodos que necesitamos o un * para todo

from modulos.funciones_matematicas import *
from modulos.modulo_coche import *

sumar(4, 65)

restar(4,99)

multipliar(3, 5)

#uso de clases que defini en otro modulo
miCoche=Coche()
miCoche.arrancar(True)
print(miCoche.estado())