#cadenas y metodos String. Doc oficial:  http://pyspanishdoc.sourceforge.net/lib/string-methods.html

name="Jose1"

print(name.capitalize())#deja solo la primera letra en mayuscula

print(name.upper())#todo a mayuscula
print(name.lower())#todo a minuscula

print(name.count("m"))#retorna la cantidad de veces que aparece la letra del parametro

print(name.isalnum())#devuelve true si la cadena es alfanumerica


s = "28212"
print(s.isdigit())#devuelve true si la cadena tiene solo un numero


print("#####################")

oracion="Estamos haciendo un reapaso de los metdoso del objeto String en python"
print(oracion.find("tamos"))#devuelve la cantidad de caracteres que hay anterior a los buscado
print(oracion.index("h"))#devuelve la posicion de la letra indicada por parametro, partiedo desde cero

print(oracion.replace("mos", "MOS"))#remplazo algo del string por otra cosa indicada




