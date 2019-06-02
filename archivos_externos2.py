from io import open

#punteros en el texto

archivo_texto=open('archivo.txt', 'r+') #lectura/escritura 

print(archivo_texto.read())

archivo_texto.seek(0) #vuelvo el curso a la posicion 0 para que pueda ser leido nuevamente en la misma ejecucion

print(archivo_texto.read())

archivo_texto.seek(11)#el cursor se vuelve a la posicion 11

print(archivo_texto.read())

archivo_texto.seek(0)#vuelvo el puntero a 0

print(archivo_texto.read(10))#leo hasta el caracter 10

#insertar textp desde la posicion determinada por el seek
archivo_texto.seek(10)#vuelvo el puntero a 10

archivo_texto.write('ME METI EN EL MEDIO DEL TEXTO')#inserto el texto desde la posicion 10 donde lo dejo el seek

archivo_texto.close()