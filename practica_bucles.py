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
