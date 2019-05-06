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


# La clase Moto hereda de Vehiculo

class Moto(Vehiculo):
    pass


miMoto=Moto("Honda", "cbr")

miMoto.estado()


