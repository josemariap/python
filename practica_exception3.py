# crear nuestras propias exceptions con raise:podemos lanzar exception ya definidas en python como clases ejemplo ZeroDivisionError o nuestros crear nuestras propias clases de Excpetion y lanzarlas
# capturamos nuestra propia exception
import math


def evaluaEdad(edad):
	if edad <0:
		raise TypeError("No se permiten edades negativas")

	if edad <20:
		return "Eres muy joven"
	elif edad <40:
		return "Eres joven"
	elif edad <65:
		return "Eres maduro"
	elif edad <100:
		return "Cuidate.."

print(evaluaEdad(2))

def calculaRaiz(num1):
	if num1 <0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

try:
	print(calculaRaiz(-2))
	
except ValueError as ErroNumeroNegativo:
    print(ErroNumeroNegativo)

print("Fin del programa")

