# clases

class Coche():

    #Constructor. defino los atributos de la calse directamente en el constructor
    def __init__(self):
    	 self.largochasis=255
    	 self.anchoChasis=4
    	 self.__ruedas=4    #doble guion sirve para encapsular o hacer private el atributo/variable
    	 self.enmarcha=False

    def arrancar(self, arrancamos):  #self = this
        self.enmarcha=arrancamos
        if(self.enmarcha):
        	return "El auto esta en marcha"
        else:
        	return "El auto esta detenido"

  
    def estado(self):
        if(self.enmarcha):
            return "El auto esta en marcha"
        else:
            return "El auto esta parado"

    def canTRuedas(self):
        return self.__ruedas #cuando quiero acceder al atributo privado uso tambien doble guion junto el col self



#################################################

miCoche=Coche()  #instancia de clase

print("El largo de mi coche es :", miCoche.largochasis)
print("El coche tiene :", miCoche.canTRuedas(), " ruedas") #cuando quiero acceder al atributo privado uso tambien doble guion y seria como un geter

print(miCoche.arrancar(False))

print("El auto esta en marcha", miCoche.enmarcha)
print(miCoche.estado())

print("Segundo objeto")

miCoche2=Coche()
miCoche2.arrancar(True)
print(miCoche2.estado())

