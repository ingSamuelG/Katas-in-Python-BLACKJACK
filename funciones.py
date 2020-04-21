import random

mazo=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
tipo=["C","S","H","D"]

def unir_listas(lista,k=0):
	milista=[]

	if k < len(lista):
		resultado=lista[k]+unir_listas(lista,k+1)
		return resultado
	else:
		return []

def reparte_cartas(lista_cartas):

	mano=random.sample(lista_cartas, 2)

	for carta in mano:
		lista_cartas.remove(carta)

	casa=random.sample(lista_cartas, 2)

	for carta in casa:
		lista_cartas.remove(carta)

	return [mano,casa,lista_cartas]


def construir_maso():

	mapa=map(lambda x: list(map(lambda y:x+y,tipo)), mazo)
	listamapa=list(mapa)
	elmazo=unir_listas(listamapa)
	return reparte_cartas(elmazo)


