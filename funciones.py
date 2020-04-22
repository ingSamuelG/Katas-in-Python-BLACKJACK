import random

mazo=["A","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","T","J","Q","K"]
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

def pedir_carta(maso):
	carta_repartir=random.sample(maso, 1)
	maso.remove(carta_repartir[0])
	return [carta_repartir[0], maso]

def dame_valor(carta):

	if carta.startswith("A"):
		return 1
	elif carta.startswith("DOS"):
		return 2
	elif carta.startswith("TRES"):
		return 3
	elif carta.startswith("CUATRO"):
		return 4
	elif carta.startswith("CINCO"):
		return 5
	elif carta.startswith("SEIS"):
		return 6
	elif carta.startswith("SIETE"):
		return 7
	elif carta.startswith("OCHO"):
		return 8
	elif carta.startswith("NUEVE"):
		return 9
	elif carta.startswith("T") or carta.startswith("J") or carta.startswith("Q") or carta.startswith("K"):
		return 10

def decide():

	return random.choice([True, False])



