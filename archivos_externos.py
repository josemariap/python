from io import open

#crear un archvio externo usando io de python y el metodo open

#lo abrimos con escritura, pero si tiene algo escrito sera pisado por lo nuevo
archivo_texto=open('archivo.txt', 'w')  #abrimos un archivo que se llamara como el primer argumento, y sera para escritura 'w'

frase="Estupendo dia para estudiar pyhton \n hasta que se haga de noche."


#escribir en el archivo antes creado
archivo_texto.write(frase) 
archivo_texto.close()#cerramos el archivo

archivo_texto_lectura=open('archivo.txt', 'r')#lo abrimos solo para lectura
#texto=archivo_texto_lectura.read()#lo leemos

texto_lineas=archivo_texto_lectura.readlines()#lo leemos linea a linea en una lista

print(archivo_texto_lectura.name)

#lo abrimos pero podemos agregar contenido sin perder lo anterior
archivo_texto_append=open('archivo.txt', 'a') #append 
fraseAppend="\n estamos agregando mas cosas sin perder lo que estaba escrito en el archivo"
archivo_texto_append.write(fraseAppend)

archivo_texto_lectura.close

#print(texto)
print(texto_lineas)
print(texto_lineas[1])
print(archivo_texto_append)




