class node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class pila:
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo_nodo = node(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamanio += 1

    def pop(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        else:
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            self.tamanio -= 1
            return dato

    def peek(self):
        if not self.esta_vacia():
            return self.tope.dato
        else:
            raise Exception("La pila está vacía")

    def evaluar_expresion(expresion):
        pila = pila()
        tokens = expresion.split()

        operadores = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "//": lambda a, b: a // b,
            "%": lambda a, b: a % b,
            "**": lambda a, b: a ** b
        }