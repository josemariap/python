# para serializar y deserializar instalar la biblioteca pickle dump() y load()

import pickle

#serializar una lista, esta lista se pasará a binaria para su rapido transporte por la red
lista_nombres = ["jose", "juan", "Ailen", "luca"]

#esta lista en binaria irá al un fichero externo
fichero_binario=open("lista_nombres", "wb")  #permisos de escritura binaria para el archivo lista_nombres

#ya tenemos el fichero externo y la lista, ahora volcamos en binario el arreglo al fichero

pickle.dump(lista_nombres, fichero_binario)# argm: lo que serializamos y donde se guardara el binario


fichero_binario.close()#cerramos
del(fichero_binario)#borramos de memoria

#al ajecutar se creará el fichero lista_nombres con el binario del arreglo!
##################################################################################

#ahora vamos a leer el archivo bibnario

fichero=open("lista_nombres", "rb")#permisos de lectura binaria
lista = pickle.load(fichero)#load lo pasa de binario a un arreglo

print(lista)