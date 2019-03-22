# tuplas: mas rapidas pero son inmutables, no son modificables, usan ( ) opcionales pero se accede al valor por indice con []

mi_tupla = ("juan", "jose", "ramiro", 5, "jose")

print(mi_tupla)

print(mi_tupla[1])

milista = list(mi_tupla)  ## con el metodo list() convertimos la tupla en una lista y ya la podriamos modificar y luego volverla a convertir en tupla

print(milista[:]) 

print(mi_tupla)

mitupla = tuple(milista) # con el metodo tuple() convertimos la lista en una tupla

print(mitupla)

print("juan" in mitupla)

print(mitupla.count("jose")) # cuenta cuantas veces se encuentra un elemento dentro de la tupla

print(len(mitupla)) # nos dice cuantos elementos tenemos

tuplaUnitaria = ("jose",) #tupla de un solo elemento, hay que clocar la "," al final

tupla2 = "juan", 3, 4, 5, 3.3 # tupla sin parentesis, es lo mismo

print(tupla2)

tuplaFecha = ("junio", 30, 2019)

mes, dia, anio = tuplaFecha # extraigo en cada variable los elementos de la tupla, siguiendo el orden

print(mes)
print(dia)
print(anio)

