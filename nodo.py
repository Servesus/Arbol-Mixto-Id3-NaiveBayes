class Nodo:
    def __init__(self,nombre,padre,arista=None):
        self.arista = arista
        self.nombre = nombre
        self.padre = padre
        self.hijos = []

    def get_hijo_arista(self,arista):
        for hijo in self.hijos:
            if hijo.arista == arista:
                return hijo