# diccionario: array asociativo, clave:valor, para operaciones de delete, add y ver valores usamos corchetes

midiccionario = {"España": "Madrid", "Francia":"Paris", "Reino Unido":"Londres"}
print(midiccionario["Francia"])

midiccionario["Italia"] = "Roma" #sirve tanto para agregar un nuevo elemento y para modificar existenes
print(midiccionario["Italia"])

print(midiccionario)

del midiccionario["Reino Unido"] # eliminamos un elemento con del
print(midiccionario)

midiccionario2 = {"Edad1": 36, 34: "Yo"} #la clave puede no tener comillas
print(midiccionario2["Edad1"])
print(midiccionario2[34])

##Defino un tupla y puedo usar un elemento de esta tuplo como clave de un diccionario
mi_tupla = ("juan", "jose", "ramiro", 5, "jose")
midiccionario[mi_tupla[1]] = "Developer" #uso de clave pata el dicc. un elemento de la tupla
print(midiccionario)

midiccionario3 = {"momnbre" : "axl", "edad": 50, "gustos": ["guns", "nirvana", "pink floyd"]} # una clave d eun dicc. puede tener de valor una lista o una tupla
print(midiccionario3)

print(midiccionario.keys()) #ver todas las claves
print(midiccionario.values()) #ver todos los valores
print(len(midiccionario)) # cantidad de elementos



