
# exceptions

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
	 	print("No esta permitido la division por 0")
	 	return "Error en la operación"

while True:
    try:
	    op1=(int(input("Introduce el primer número: ")))
	    op2=(int(input("Introduce el segundo número: ")))
	    break
          
    except ValueError:
        print("No se puede ingresar letras")
		

	
		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Continua la ejecución del programa..")

