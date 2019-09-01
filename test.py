from arbol_mixto import ArbolMixto as a
from nodo import Nodo
"""
#Test para imprimir arbol como grafo

#import networkx as nx
#import matplotlib.pyplot as plt
cielo = Nodo("Cielo",None)
humedad = Nodo("Humedad",cielo,"Soleado")
positivoNublado = Nodo("+",cielo,"Nublado")
viento = Nodo("Viento",cielo,"Lluvia")
negativoAlta = Nodo("-",humedad,"Alta")
positivoNormal = Nodo("+",humedad,"Normal")
negativoFuerte = Nodo("-",viento,"Fuerte")
positivoDebil = Nodo("+",viento,"Debil")

cielo.hijos = [humedad,positivoNublado,viento]
humedad.hijos = [negativoAlta,positivoNormal]
viento.hijos = [negativoFuerte,positivoDebil]

t = a()

t.nodos = [cielo,humedad,positivoNublado,viento,negativoAlta,positivoNormal,negativoFuerte,positivoDebil]
t.dibuja_arbol()

G = t.convertir_arbol_grafo()
nx.draw(G,with_labels=True)
plt.show()




Test para probar a cargar datos y calcular entropia


t = a()
datos = t.get_datos(True,"datasets/ejemplo1.csv")
#print(datos.head(10))

print(t.get_entropia(datos))

print(datos.iloc[0,0])
print(datos.loc[0,"Cielo"])
print(list(datos.columns))


b = datos['Temperatura']
list_atributos = list(set(b))
nuevos_datos = datos.loc[datos["Temperatura"] == "alta"]
print(nuevos_datos)
print(len(nuevos_datos.index))

print(t.get_entropia(datos))
print(t.get_ganancia(datos, 'Humedad'))
print(t.get_ganancia(datos, 'Viento'))
print(t.get_ganancia(datos, 'Cielo'))
print(t.get_ganancia(datos,"Temperatura"))

t.atributos = list(datos.columns)
del t.atributos[-1]
print(datos.columns)
print(datos[t.get_mejor_atributo(datos)])
ultima_columna = datos.iloc[:,-1]
print(list(ultima_columna.mode())[0])

"""

t = a()
t.entrenar(True,"datasets/ejemplo1.csv",3)
t.dibuja_arbol()
res = t.clasificar(True,"datasets/ejemplo1.csv")
print(t.get_datos(True,"datasets/ejemplo1.csv"))
print(res)