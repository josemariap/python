# paquetes distribuibles, creamos con esta configuracion con la funcion de python setup,  haremos un paquete destribuible con las funciones de calculos_generales.py
# se instala en nuestro python local
# le indicamos el archivo o directorio que haremos un paquete distribuible con lo que indequemos dentro de package[]
# por consola nos paramos en este setup.py y ejecutamos: python setup.py sdist   ,nos crea una carpeta dist con el compirmido.tar de nuestro paquete que es el que podremos distribuir
# este paqueto comprimido se puede distribuir o instalar dentro de nuestro ordenador para uso global con python, para instalarlo nos
# paramos por consola a la par de nuestro paquete comprimido y ejecutamos: pip3 install paquetecalculos-1.0.tar.gz y se instala localmente en nustro python
# para desinstalarlo: pip3 uninstall paquetecalculos-1.0.tar.gz
# ejemplo del setup de configuracion:
from setuptools import setup

setup(

    name="paquetecalculos",
    version="1.0",
    description="paquete de calculos",
    author="jpico",
    author_email="vvvvv@ff.com",
    url="dddddd.com",
    package=["paquete_calculos", "paquete_calculos.sub_paquete"]
)