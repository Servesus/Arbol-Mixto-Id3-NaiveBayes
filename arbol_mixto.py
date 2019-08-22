import networkx as nx
from nodo import Nodo
from random import randrange
class ArbolMixto:
    def __init__(self,atributos):
        """
        Nodos contiene todos los nodos del arbol en orden de forma que el nodo en la posicion 0 es el nodo raiz.
        Atributos contiene la lista de los headers de los datos, en caso de tener que ir modificando hacer una copia de esta lista.
        """
        self.nodos = []
        self.atributos = atributos

    def convertir_arbol_grafo(self):
        """
        Convierte el arbol de un grafo usando NetworkX, asi se puede imprimir por pantalla.
        """
        G = nx.Graph()
        G.add_node(str(self.nodos[0].nombre))
        for nodo in self.nodos:
            for hijo in nodo.hijos:
                G.add_node(str(hijo.nombre),attribute=randrange(1000))
                G.add_edge(str(nodo.nombre),str(hijo.nombre),label=str(hijo.arista))


        return G


