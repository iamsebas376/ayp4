class node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo_nodo = node(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.esta_vacia():
            return None
        else:
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            return dato

    def peek(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.dato

def infija_a_postfija(expresion):

    precedencia = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "//": 2,
        "%": 2,
        "**": 3
    }

    salida = []
    pila_operadores = pila()

    tokens = expresion.split()

    for token in tokens:

        if token.lstrip("-").replace(".", "").isdigit():
            salida.append(token)
            print(f"Token '{token}' es un número, se agrega a la salida.")

        elif token == "(":
            pila_operadores.push(token)
            print(f"Token '{token}' es parentesis de inicio, se agrega a la pila de operadores.")

        elif token == ")":
            while not pila_operadores.esta_vacia() and pila_operadores.peek() != "(":
                operador = pila_operadores.pop()
                salida.append(operador)
            pila_operadores.pop()  # Desapilar el '('
            print(f"Token '{token}' es parentesis de cierre, se desapilan operadores hasta encontrar '('.")

        elif token in precedencia:
            while (not pila_operadores.esta_vacia() and pila_operadores.peek() != "(" and
                pila_operadores.peek() in precedencia and (precedencia[pila_operadores.peek()] >= precedencia[token])):
                operador = pila_operadores.pop()
                salida.append(operador)
            pila_operadores.push(token)
            print(f"Token '{token}' es un operador, se maneja la precedencia y se agrega a la pila de operadores.")

    while not pila_operadores.esta_vacia():
        operador = pila_operadores.pop()
        salida.append(operador)
        print(f"Se desapilan los operadores restantes en la pila y se agregan a la salida.")


    salida = " ".join(salida)
    print(f"Expresión infija: '{expresion}' se convierte a postfija: '{salida}'")

            

infija_a_postfija("3 + ( 5 * 2 )")