from arbol_mixto import ArbolMixto as a
from nodo import Nodo
"""
Test para imprimir arbol como grafo

#import networkx as nx
#import matplotlib.pyplot as plt
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

t = a()

t.nodos = [cielo,humedad,positivoNublado,viento,negativoAlta,positivoNormal,negativoFuerte,positivoDebil]
G = t.convertir_arbol_grafo()
nx.draw(G,with_labels=True)
plt.show()

"""

"""
Test para probar a cargar datos y calcular entropia
"""

t = a()
datos = t.get_datos(True,"datasets/ejemplo1.csv")
print(datos.head(10))

print(t.get_entropia(datos))

print(datos.iloc[0,0])
print(datos.loc[0,"Cielo"])
print(list(datos.columns))
