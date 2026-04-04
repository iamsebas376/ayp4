"""
EJERCICIOS DE PILAS Y COLAS (STACKS & QUEUES)
--------------------------------------------
Implementado sin usar list[] de Python.
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Pila:
    def __init__(self):
        self.tope = None

    def push(self, x):
        nuevo = Nodo(x)
        nuevo.sig = self.tope
        self.tope = nuevo

    def pop(self):
        if self.esta_vacia(): return None
        v = self.tope.dato
        self.tope = self.tope.sig
        return v

    def esta_vacia(self):
        return self.tope is None

# 1. EJERCICIO: Paréntesis Balanceados
def balanceados(cadena):
    p = Pila()
    for char in cadena:
        if char == "(":
            p.push(char)
        elif char == ")":
            if p.pop() is None: return False
    return p.esta_vacia()

# 2. EJERCICIO: Decimal a Binario con Pila
def decimal_a_binario(n):
    p = Pila()
    while n > 0:
        p.push(n % 2)
        n //= 2
    
    binario = ""
    while not p.esta_vacia():
        binario += str(p.pop())
    return binario or "0"

class Cola:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def enqueue(self, x):
        nuevo = Nodo(x)
        if self.fin:
            self.fin.sig = nuevo
        self.fin = nuevo
        if self.inicio is None:
            self.inicio = nuevo

    def dequeue(self):
        if self.inicio is None: return None
        v = self.inicio.dato
        self.inicio = self.inicio.sig
        if self.inicio is None:
            self.fin = None
        return v

# 3. EJERCICIO: Invertir Cola con Pila
def invertir_cola(cola):
    p = Pila()
    while cola.inicio:
        p.push(cola.dequeue())
    while not p.esta_vacia():
        cola.enqueue(p.pop())

if __name__ == "__main__":
    print(f"¿'((()))' balanceado?: {balanceados('((()))')}")
    print(f"¿'(()' balanceado?: {balanceados('(()')}")
    print(f"13 en binario: {decimal_a_binario(13)}")
    
    c = Cola()
    for i in range(1, 4): c.enqueue(i)
    invertir_cola(c)
    print(f"Cola invertida (primero): {c.dequeue()}")
