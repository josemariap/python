def divide():
	try:
		op1=(float(input("Introduce el primer numero")))
		op2=(float(input("Introduce el segundo numero")))
		print("La division es:" + str(op1/op2))
		
	except ValueError:
		print("El valor ingresado es invalido")
	except ZeroDivisionError:
		print("No esta permitido dividir por 0")
	except:
		print("Ocurrio un error no contenplado")
	
	finally:
		print("Claculo finalizado")
	

divide()