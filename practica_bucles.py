# bucles
index = 0
for i in [1, 2, 3, 4, "Hello"]:
	print(i)#imprime los elementos de la lista
	print(i, end="")#imprime todo en una linea


#Validar que el mail tenga un @ y un punto
email=0
miEmail="josepicoas@gmail.com"

for i in miEmail:
	print(i)#imprime cada uno de los caracteres del string
	if(i=="@" or i=="."):
		email=email+1

if(email==2):
   print("El mail es valido")  
else:
   print("El mail no es valido")


#range
for i in range(8): #racorre rango del 0 al 7
	print(i)
	print(f"La posicion de la lista contiene: {i} " ) #unimos en un string texto mas valor de variable


for i in range(3,9): #racorre rango del 3 al 8
	print(i)

for i in range(4,40, 2): #racorre rango del 4 al 39 con salto de 2
	print(i)


print("**********************************************************")

name=[1,3,5,2,66,7]
#range con lenght
for i in range(len(name)): #recorro la longitud de la lista
    print(name[i]) 

#################################

# continue y pass
for i in range(4,40, 2): #racorre rango del 4 al 39 con salto de 2
    if i == 10:##i con valor 10 será ignorado
      continue #ignora lo que queda por hacer en esa vuelta de bucle y pasa a la siguiente iteracion
    print(i)


for i in range(4,40, 2): 
    if i == 10:
      break #sale del for totalmente
    print(i)



