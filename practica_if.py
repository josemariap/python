# condicionales
print("Programa de evaluacion de notas")

nota_alumno = input("Introduce la nota..") #las entradas por consola entran como String

def evaluacion(note):
	valoracion =  "aprobado"
	if note < 5 :
		valoracion = "suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))  #casteo la entrada a int

