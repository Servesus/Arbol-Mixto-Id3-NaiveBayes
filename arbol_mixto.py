import networkx as nx
from nodo import Nodo
import pandas
import math

class ArbolMixto:
    def __init__(self):
        """
        Nodos contiene todos los nodos del arbol en orden de forma que el nodo en la posicion 0 es el nodo raiz.
        Atributos contiene la lista de los headers de los datos, en caso de tener que ir modificando hacer una copia de esta lista.
        """
        self.nodos = []
        self.atributos = None

    def convertir_arbol_grafo(self):
        """
        Convierte el arbol de un grafo usando NetworkX, asi se puede imprimir por pantalla.
        """
        G = nx.Graph()
        G.add_node(self.nodos[0])
        for nodo in self.nodos:
            for hijo in nodo.hijos:
                G.add_node(hijo)
                G.add_edge(nodo,hijo.nombre,label=hijo.arista)


        return G

    def get_datos(self,headers,ruta):
        """
        El csv con los datos debe tener en la ultima columna el atributo clasificador
        Headers debe ser true si el csv contiene headers, false en otro caso
        Para que funcione correctamente la ruta, meter csv en carpeta datasets y pasar la ruta como
        "datasets/cars.csv" con las comillas y cambiar cars.csv por el nombre que sea
        Devuelve los datos como dataframe
        """
        r = str(ruta)
        if headers == False:
            datos = pandas.read_csv(r, header=None)
        if headers == True:
            datos = pandas.read_csv(r)

        return datos

    def get_entropia(self,datos):
        """
        Recibe como parametro los datos como dataframe devuelve la entropia del dataset
        """
        columna = datos.iloc[:,-1]  
        valores = list(set(columna))
        p = 0
        for i in columna:
            if i == valores[0]:
                p = p + 1
        n = len(columna) - p
        division1 = p/len(columna)
        division2 = n/len(columna)
        entropia = - (division1 * math.log(division1,2)) - (division2 * math.log(division2,2))
        return entropia



