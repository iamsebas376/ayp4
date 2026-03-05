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
            return None
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

    @staticmethod
    def evaluar_expresion(expresion):
        pila_inst = pila()
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

        for token in tokens:
            if token.lstrip("-").replace(".", "").isdigit():
                pila_inst.push(float(token))
            elif token in operadores:
                b = pila_inst.pop()
                a = pila_inst.pop()
                resultado = operadores[token](a, b)
                pila_inst.push(resultado)
            else:
                raise Exception(f"Token no reconocido: {token}")
        return pila_inst.pop()
    
# Ejemplo de uso
if __name__ == "__main__":
    expresion = "3 4 + 2 * 7 -"
    resultado = pila.evaluar_expresion(expresion)
    print(f"El resultado de la expresión '{expresion}' es: {resultado}")