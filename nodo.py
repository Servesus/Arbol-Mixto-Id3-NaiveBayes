class Nodo:
    def __init__(self,nombre,padre,arista=None):
        self.arista = arista
        self.nombre = nombre
        self.padre = padre
        self.hijos = []

    def __str__(self):
        if self.arista != None:
            res ="( " + self.arista+ " ) " + self.nombre
        else:
            res = self.nombre
        return res