# condicionales
print("Programa de evaluacion de notas")

nota_alumno = input("Introduce la nota..") #las entradas por consola entran como String

def evaluacion(note):
	valoracion =  "aprobado"
	if note < 5 :
		valoracion = "suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))  #casteo la entrada a int


# if-else
edad = int(input("Introduce tu edad"))

if edad >= 18:
	print("Puedes pasar")
else:
	print("No pudes pasar")

print("Fin")

# elif

edad2 = int(input("Introduce tu edad"))

if edad2 < 18:
	print("No Puedes Pasar")
elif edad2 < 21:
	print("Queda a tu criterio")
else:
	print("Ok puedes pasar!")

print("Fin")



