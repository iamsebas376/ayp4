#Constructor de la clase Nodo
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

#Clase Lista simple
class Lista:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        if self.cabeza is None:
            self.cabeza = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=' -> ')
            nodo_actual = nodo_actual.siguiente

#Insertar nodos
mi_lista = Lista()
mi_lista.insertar(4)
mi_lista.insertar(5)
mi_lista.insertar(6)

#Imprimir nodos
mi_lista.imprimir()