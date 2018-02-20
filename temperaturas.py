from lxml import etree
from urllib.request import urlopen
from temperaturas1 import localidad,nombrelocal,listado

contador=0

cp=input("Dime el Codido Postal de la localidad que desee: ")
url=('http://www.aemet.es/xml/municipios/localidad_%s.xml' % (cp))

for city in listado():
	if city == nombrelocal(url):
		contador=contador+1

if contador == 1:
	localidad(url)
else:
	print("Error, la ciudad que intentas buscar no se encuentra.")
	
#http://www.aemet.es/xml/municipios/localidad_41038.xml
#sevilla.xml