#  concatenamos condicionales, no existe el switch pero se remplaza and, or

edad = 1

if 0 < edad < 100:
	print("Edad es corracta")
else:
	print("Edad es incorrecta")

salario_jefe_area = int(input("Introduce el salario del jefe del area"))
print("Salario jefe area:"  + str(salario_jefe_area))


salario_presi = int(input("Introduce el salario del presidente"))
print("Salario presidente:"  + str(salario_presi))

salario_admin = int(input("Introduce el salario del administrativo"))
print("Salario administrativo:"  + str(salario_admin))

if salario_admin < salario_jefe_area < salario_presi:
	print("Todo funciona correacto")
else:
	print("Algo anda mal en esta empresa")