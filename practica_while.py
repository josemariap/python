# while

print("hola")

i=1

while i<=10:
	print(i)
	i=i+1

edad=int(input("Ingresa tu edad"))

while edad < 18 or edad > 99:
	edad=int(input("La edad no es correcta, ingresa de nuevo tu edad..."))


print("Puedes ingresar, tu edad es correcta ya que tienes " + str(edad))