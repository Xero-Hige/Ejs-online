class _Nodo:
    def __init__(self, dato = None, prox = None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

