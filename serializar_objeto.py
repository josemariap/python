import pickle
#gardaremos los objetos de coche en un arreglo y eso lo serializaremos
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarca=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarca=True
        
    def frenar(self):
        self.frena=True
        
    def acelerar(self):
        self.celera=True
        
    def estado(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "En marcha: ", self.enmarca, "Acelerando: ", self.acelera, "Frenando: ", self.frena)

coche1=Vehiculo("Mazda", "x7")
coche2=Vehiculo("Ferrari", "Modena")
coche3=Vehiculo("RedBull", "De Verstapens")

coches=[coche1, coche2, coche3]

#Serializamos el arreglo de coches
fichero=open("loscoches", 'wb')#permisos de escritura binaria

pickle.dump(coches, fichero)#serializamos el arreglo de autos en el archivo losCoches

#ceeramos y borramos de memoria
fichero.close()
del(fichero)

#usamos nuestro archivo que esta serializado con el arreglo de coches
ficheroApertura=open('loscoches', 'rb')
misCoches=pickle.load(ficheroApertura)#leemos los bytes del archivo, que es el arreglo
ficheroApertura.close()

#mostramos los coches
for c in misCoches:
    print(c.estado())

