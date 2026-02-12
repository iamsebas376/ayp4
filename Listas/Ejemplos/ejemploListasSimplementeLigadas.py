class Nodo:
    def __init__ (self, nombre, cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.siguiente = None

class Lista:
    def __init__ (self):
        self.cabeza = None

    def insertarFinal(self, nombre, cedula):
        nuevoNodo = Nodo(nombre, cedula)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo
        print("Nodo agregado exitosamente.")

    def insertarPrioridad(self, nombre, cedula, prioridad):
        nuevoNodo = Nodo(nombre, cedula, prioridad)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        elif self.cabeza.prioridad > prioridad:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza 
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevoNodo.siguiente = actual.siguiente
            actual.siguiente = nuevoNodo
        print("Nodo con prioridad agregado exitosamente.") 

    def imprimirLista(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre, actual.cedula, actual.prioridad, end=" ---> ")
            actual = actual.siguiente

lista = Lista()
lista.insertarPrioridad("Sebastián", 1001478559, 1)
lista.insertarPrioridad("Sebastián", 1001478559, 3)
lista.insertarPrioridad("Sebastián", 1001478559, 2)
lista.imprimirLista()