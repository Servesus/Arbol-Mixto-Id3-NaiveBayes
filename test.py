from arbol_mixto import ArbolMixto as a
from nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt

cielo = Nodo("Cielo")
humedad = Nodo("Humedad","Soleado")
positivoNublado = Nodo("+","Nublado")
viento = Nodo("Viento","Lluvia")
negativoAlta = Nodo("-","Alta")
positivoNormal = Nodo("+","Normal")
negativoFuerte = Nodo("-","Fuerte")
positivoDebil = Nodo("+","Debil")

cielo.hijos = [humedad,positivoNublado,viento]
humedad.hijos = [negativoAlta,positivoNormal]
viento.hijos = [negativoFuerte,positivoDebil]

t = a([])

t.nodos = [cielo,humedad,positivoNublado,viento,negativoAlta,positivoNormal,negativoFuerte,positivoDebil]
G = t.convertir_arbol_grafo()
nx.draw(G,with_labels=True)
plt.show()