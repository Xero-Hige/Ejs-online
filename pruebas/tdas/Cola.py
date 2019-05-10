class Cola:
    def __init__(self):
        self.prim = None
        self.ult = None 
    
    def encolar(self, elemeto):
        nodo = _Nodo(elemento)
        if not self.prim:
            self.prim = nodo
        else:
            self.ult.prox = nodo
        self.ult = nodo

    def desencolar(self):
        if not self.prim:
            raise ValueError("La cola está vacía")
        valor = self.prim.dato
        self.prim = self.prim.prox
        if not self.prim:
            self.ult = None
        return valor

    def esta_vacia(self):
        return self.prim is None