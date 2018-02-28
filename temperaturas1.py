from lxml import etree
from urllib.request import urlopen


#extrae codigo
def extracodigo(busqueda):

	url = ('http://josedom24.github.io/mod/lm/fich/sevilla.xml')
	response = urlopen(url)
	doc = etree.parse(response)
	xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

	raiz=doc.getroot()

	for i in range(len(raiz)):
		provincia=raiz[i]
		municipio = provincia.text
		municipio = municipio.lower() #nombre

		for attr,value in provincia.items():
			nombre=(attr,value)
			nombre=nombre[1]
			nombre=nombre.split('-')
			nombre=nombre[0]
			nombre=nombre.lower()  #nombre
			
			if busqueda == nombre or busqueda == municipio:
				for attr,value in provincia.items():
					codigo=(attr,value)
					codigo=codigo[1]
					codigo=codigo.split('-')
					codigo=codigo[1]
					codigo=codigo[2:]


					return(codigo)

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
