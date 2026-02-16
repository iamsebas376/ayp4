class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nodo
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def contar_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_recursivo(nodo.siguiente)
    
    def encontrar_dato(self, nodo, dato):
        if nodo is None:
            return False
        elif nodo.dato == dato:
            return True
        return self.encontrar_dato(nodo.siguiente, dato)
    
lista = Lista()

lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar("Dato")

print(lista.contar_recursivo(lista.cabeza))
print(lista.encontrar_dato(lista.cabeza, "Dato"))