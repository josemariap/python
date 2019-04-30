# clases

class Coche():
    largochasis=250
    anchoChasis=4
    ruedas=4
    enmarcha=False

    def arrancar(self):  #self = this
        self.enmarcha=True
        
    def estado(self):
        if(self.enmarcha):
            return "El auto esta en marcha"
        else:
            return "El auto esta parado"

miCoche=Coche()  #instancia de clase

print("El largo de mi coche es :", miCoche.largochasis)
print("El coche tiene :", miCoche.ruedas, " ruedas")

miCoche.arrancar()

print("El auto esta en marcha", miCoche.enmarcha)
print(miCoche.estado())