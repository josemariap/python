#herencia super 

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Lugar: ", self.lugar_residencia)

    

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugar_residencia):
        super().__init__(nombre, edad, lugar_residencia)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)


##########################

p1=Empleado(5000, 4, "Jose", 35, "bsAs")
p1.descripcion()