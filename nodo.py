class Nodo:
    def __init__(self,nombre,padre,arista=None):
        self.arista = arista
        self.nombre = nombre
        self.padre = padre
        self.hijos = []