class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self,elemento):
        self.pila.append(elemento)
    
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        self.pila.pop()

    def esta_vacia(self):
        len(self.pila) == 0
    
    def ver_tope(self):
        if self.esta_vacia:
            return None
        return self.pila[len(self.pila) - 1]
