from lxml import etree
from urllib.request import urlopen


#lista de nombres
def listado():
	
	lista=[]

	url = ('http://josedom24.github.io/mod/lm/fich/sevilla.xml')
	response = urlopen(url)
	doc = etree.parse(response)
	localidades = doc.findall("municipio")

	for i in range(len(localidades)):
		city=localidades[i].text
		lista.append(city)

	return lista




#Busca nombre
def nombrelocal(cp):
	
	response1 = urlopen(cp)
	doc1 = etree.parse(response1)
	nombre = doc1.findall("nombre")
	
	return(nombre[0].text)







#Busca temperaturas
def localidad(cp):
	
	response = urlopen(cp)
	doc = etree.parse(response)
	dia=doc.findall("prediccion/dia/temperatura")
	
	maxima=(dia[0].find("maxima").text)
	minima=(dia[0].find("minima").text)
	return print("Temperatura maxima: %s y minima: %s (HOY)" % (maxima,minima))
