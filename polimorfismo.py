# polimorfismo

print("Defino las clases")

class Coche():

	def desplazamiento(self):
		print("Uso cuatro ruedas")


class Moto():

	def desplazamiento(self):
		print("Uso dos ruedas")


class Camion():

	def desplazamiento(self):
		print("Uso muchas ruedas")


print("Finalizo definicion de las clases")
###############################################

def desplazamiento(vehiculo):
	vehiculo.desplazamiento()


camion=Camion()
auto=Coche()
moto=Moto()

desplazamiento(camion)
desplazamiento(auto)
desplazamiento(moto)

