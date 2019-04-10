# generadores, al generarse los elementos a medida que se usan, se ahorra recursos. Dependiendo los casos
def generaPares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num=num+1
	return miLista	
    
print(generaPares(20))


def generaParesGenerador(limite):
	num=1
	while num<limite:
		yield num*2  # crea un tipo de elemento que se va auto generando sin ser una lista, pero siempre hay un elemento y automaticamente retorna el yield que generará los elementos
		num=num+1
		
#asignamos el yield que solo tiene el primer elemento pero esta listo para aut generarse
devuelvePares=generaParesGenerador(20) # el yield empieza a generar los elementos y en la variable me queda todo lo que generó siempre y cuando lo recorra con un for
devuelveParesDeAuno=generaParesGenerador(20) # este vamos haciendo que se genere de a un elemento con el next

#el for hace que genere todos los elementos
for i in devuelvePares:  # genera todos los elementos pero no podremos llamar con el next de abajo elemento por elemento porque la variable devuelvePares ya se le genero todo
	print(i)

# observamos como genera de a uno los elementos a medida que lo llamamos con el next
print(next(devuelveParesDeAuno)) # pirmera generada
 
print(next(devuelveParesDeAuno)) # segunda  ""

print(next(devuelveParesDeAuno)) # tercera  ""

print("********************** yield from")

def devuelve_ciudades(*ciudades):  #el asterisco es para poder pasar la cantidad que queremos de parametros
	for elemento in ciudades:
		yield from elemento   #from hace que se genere cada elemento en el yield y a su vez los elementos de cada elemento(como dos for anidados para recorrer una matriz)


letrasCiudades=devuelve_ciudades("Roma", "Buenos aires", "Virginia")

for subElemento in letrasCiudades:
	print(subElemento)



        


