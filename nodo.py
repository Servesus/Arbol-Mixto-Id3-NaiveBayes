class Nodo:
    def __init__(self,nombre,padre,arista=None):
        self.arista = arista
        self.nombre = nombre
        self.padre = padre
        self.hijos = []

    def get_hijo_arista(self,arista):
        res = None
        for hijo in self.hijos:
            if type(hijo.arista) is int:
                x = float(hijo.arista)
                y = type(arista)(x)
                if arista == y:
                    res = hijo
            else:
                if hijo.arista == arista:
                    res = hijo
        return res