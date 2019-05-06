# herencia

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


# La clase Furgoneta hereda de Vehiculo
class Furgoneta(Vehiculo):
    cargado=False

    def carga(self, cargar):
        self.cargado=cargar
    
    #overrite del metodo estado()
    def estado(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "En marcha: ", self.enmarca, "Acelerando: ", self.acelera, "Frenando: ", self.frena, "Cargada: ", self.cargado)




# La clase Moto hereda de Vehiculo
class Moto(Vehiculo):
    hcaballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo caballito"
    
    #overrite del metodo estado()
    def estado(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "En marcha: ", self.enmarca, "Acelerando: ", self.acelera, "Frenando: ", self.frena, "Caballito: ", self.hcaballito)




############################################

miMoto=Moto("Honda", "cbr")

miMoto.caballito()
miMoto.estado()

miCamioneta=Furgoneta("Chevrolet", "C10")
miCamioneta.carga(True)
miCamioneta.estado()

# puedo tener multiple herencia
class MotoDeCarga(Moto, Furgoneta):  #hereda de Moto y de Furgoneta, toma el constructor si es que lo tiene, de la primera clase que hereda, o sea Moto
    pass