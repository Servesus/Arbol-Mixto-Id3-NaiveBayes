import networkx as nx
from nodo import Nodo
import pandas
import math
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing
import numpy

class ArbolMixto:
    def __init__(self):
        """
        Nodos contiene todos los nodos del arbol en orden de forma que el nodo en la posicion 0 es el nodo raiz.
        Atributos contiene la lista de los headers de los datos.
        """
        self.nodos = []
        self.atributos = []
        self.datos_entrenamiento = None
        self.datos_evaluacion = None
        self.clasificaciones = None 

    def crear_nodo(self,nombre,padre,arista):
        nodo = Nodo(nombre,padre,arista)
        if padre != None:
            padre.hijos.append(nodo)
        self.nodos.append(nodo)


    def dibuja_arbol(self):
       """
       Convierte el arbol mixto en un arbol de la libreria anytree para poder representarlo facilmente
       """
       from anytree import Node, RenderTree
       for nodo in self.nodos:
           if nodo.padre == None:
               vars()[nodo.nombre] = Node(nodo.nombre)
           else:
               vars()[nodo.arista] = Node(str(nodo.arista),parent = vars()[nodo.padre.nombre])
               vars()[nodo.nombre] = Node(nodo.nombre,parent = vars()[nodo.arista])
        
       for pre, fill, node in RenderTree(vars()[self.nodos[0].nombre]):
           print("%s%s" % (pre, node.name))
        

    def get_datos(self,headers,ruta):
        """
        El csv con los datos debe tener en la ultima columna el atributo clasificador
        Headers debe ser true si el csv contiene headers, false en otro caso
        Para que funcione correctamente la ruta, meter csv en carpeta datasets y pasar la ruta como "datasets/cars.csv"
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
        if p == 0 or n == 0:
            return 0
        else:
            division1 = p/len(columna)
            division2 = n/len(columna)
            entropia = - (division1 * math.log(division1,2)) - (division2 * math.log(division2,2))
            return entropia
        

    def get_ganancia(self, datos, atributo):
        """
        Recibe como parametro los datos como dataframe y el nombre del atributo del que se quiere calcular la ganancia 
        """
        list_valores_atributo = list(set(datos[atributo]))
        longitud_total = len(datos.index)
        entropia_datos = self.get_entropia(datos)
        for valor in list_valores_atributo:
            nuevos_datos = datos.loc[datos[atributo] == valor]
            longitud_valor = len(nuevos_datos.index)
            division = longitud_valor/longitud_total
            res = division * self.get_entropia(nuevos_datos)
            entropia_datos = entropia_datos - res
        return entropia_datos

                    
    def get_mejor_atributo(self,datos):
        ganancias = []
        for atributo in self.atributos:
            ganancia = self.get_ganancia(datos,atributo)
            ganancias.append(ganancia)
        indice_mejor = ganancias.index(max(ganancias))
        return self.atributos[indice_mejor]

    def entrenar(self,headers,ruta,quorum):
        """
        Parametros : headers y ruta para el metodo get_datos()
        quorum: numero minimo de ejemplos que debe contener el dataset para que la rama del arbol id3 sea fiable
        """
        datos = self.get_datos(headers,ruta)
        self.datos_entrenamiento = datos
        self.atributos = list(datos.columns)
        del self.atributos[-1]
        self.crear_arbol_mixto(datos,quorum,None,None)



    def crear_arbol_mixto(self,ejemplos,quorum,nodo_anterior,valor_anterior):
        """
        Nodo_anterior y valor_anterior son necesario para poder asignar padre y arista
        """
        #Si no se cumple en quorum añadir nodo para llamada Naive Bayes
        ultima_columna = list(set(ejemplos.iloc[:,-1]))
        if len(ejemplos.index) < quorum:
            self.crear_nodo("Naive Bayes",nodo_anterior,valor_anterior)
        #Si todos los ejemplos tienen la misma clasificacion crear nodo con dicha clasificacion
        elif len(ultima_columna) == 1:
            self.crear_nodo(str(ultima_columna[0]),nodo_anterior,valor_anterior)
        #Si no quedan atributos devolver valor mayoritario
        elif len(self.atributos) <= 0:
            #Saco la ultima columna como dataframe para poder sacar el valor mas comun
            df_ultima_columna = ejemplos.iloc[:,-1]
            valor_mayoritario = list(df_ultima_columna.mode())[0]
            self.crear_nodo(str(valor_mayoritario),nodo_anterior,valor_anterior)
        else:
            mejor_atributo = self.get_mejor_atributo(ejemplos)
            valores_mejor_atributo = list(set(ejemplos[mejor_atributo]))
            self.crear_nodo(mejor_atributo,nodo_anterior,valor_anterior)
            nodo = self.nodos[-1]
            self.atributos.remove(mejor_atributo)
            for valor in valores_mejor_atributo:
                nuevos_ejemplos = ejemplos.loc[ejemplos[mejor_atributo] == valor]
                #Si el nuevo conjunto esta vacio añado nodo con valor mayoritario solo en caso de que el quorum sea 0 ya que si fuese mayor que 0 le corresponderia un 
                # nodo naive bayes porque no alcanzaria el minimo
                if len(nuevos_ejemplos.index) == 0 and quorum == 0:
                    df_ultima_columna = ejemplos.iloc[:,-1]
                    valor_mayoritario = list(df_ultima_columna.mode())[0]
                    self.crear_nodo(str(valor_mayoritario),nodo_anterior,valor)
                else:
                    self.crear_arbol_mixto(nuevos_ejemplos,quorum,nodo,valor)

    def clasificar(self,header,ruta):
        """
        Recibe como parametros los mismos que el metodo get_datos()
        Devuelve una lista con la clasificacion para cada fila
        """
        datos = self.get_datos(header,ruta)
        self.datos_evaluacion = datos
        res = []
        for i in range(len(datos.index)):
            fila = datos.iloc[i,:]
            clasificacion = self.clasifica_fila(fila,self.nodos[0])
            res.append(clasificacion)
        self.clasificaciones = res
        return res

    def clasifica_fila(self,fila,nodo):
        if nodo.nombre == "Naive Bayes":
            #TODO Hacer naive Bayes con scikit-learn
            return self.naive_bayes(fila)
        elif len(nodo.hijos) == 0:
            return str(nodo.nombre)
        else:
            siguiente_nodo = nodo.get_hijo_arista(str(fila[nodo.nombre]))
            return self.clasifica_fila(fila,siguiente_nodo)


    def naive_bayes(self,fila):
        res = []
        solucion = []
        tamaño_inicial = len(self.datos_entrenamiento.index)
        ultima_columna = list(set(self.datos_entrenamiento.iloc[:,-1]))
        atributos = list(self.datos_entrenamiento.columns)
        atributo_objetivo = atributos[-1]
        del atributos[-1]
        for valor in ultima_columna:
            probabilidad = 1
            datos_filtrados = self.datos_entrenamiento.loc[self.datos_entrenamiento[atributo_objetivo] == valor]
            probabilidad = probabilidad * ((len(datos_filtrados.index)+1)/(tamaño_inicial + 2))
            for atributo in atributos:
                datos_filtrados2 = datos_filtrados.loc[datos_filtrados[atributo] == fila[atributo]]
                probabilidad = probabilidad * ((len(datos_filtrados2.index)+1)/(tamaño_inicial + 2))
            res.append(round(probabilidad,5))
        solucion.append(ultima_columna[res.index(max(res))])
        solucion.append(max(res))
        return solucion

    def rendimiento(self):
        """
        Compara la ultima columna de los datos de evaluacion con las clasificaciones del arbol mixto, devuelve el porcentaje de acierto
        """
        ultima_columna = list(self.datos_evaluacion.iloc[:,-1])
        aciertos = 0
        for i,valor in enumerate(ultima_columna):
            if type(self.clasificaciones[i]) is list:
                clasificacion = self.clasificaciones[i][0]
            else:
                clasificacion = self.clasificaciones[i]
            if clasificacion == valor:
                aciertos = aciertos + 1
        
        return (aciertos / len(ultima_columna))*100


