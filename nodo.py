class Nodo:
    def __init__(self,nombre,arista=None):
        self.arista = arista
        self.nombre = nombre
        self.hijos = []