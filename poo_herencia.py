# herencia

class Vehiculo():
    def __init_(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarca=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.arrancar=True
        
    def frenar(self):
        self.frena=True
        
    def acelerar(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\n En marcha: ", self.enmarca, "\n Acelerando: ", self.acelera, "\n Frenando: ", self.frena)


# LA clase Moto hereda de Vehiculo

class Moto(Vehiculo):
    pass




