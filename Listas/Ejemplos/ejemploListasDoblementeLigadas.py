class Node:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nodoNuevo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nodoNuevo
            self.cola = nodoNuevo
        else:
            nodoNuevo.siguiente = self.cabeza
            self.cabeza.anterior = nodoNuevo
            self.cabeza = nodoNuevo

    def insertar_final(self, dato):
        nodoNuevo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nodoNuevo
            self.cola = nodoNuevo
        else:
            self.cola.siguiente = nodoNuevo
            nodoNuevo.anterior = self.cola
            self.cola = nodoNuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    def eliminar_final(self):
        if self.esta_vacia():
            return None

        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    def recorrer_adelante(self):
        if self.esta_vacia():
            return "Lista vacia"
        
        print("Recorriendo de Inicio a Fin")
        actual = self.cabeza
        while actual:
            print(actual.dato, end =" -> ")
            actual = actual.siguiente
        print("Fin")

    def recorrer_atras(self):
        if self.esta_vacia():
            return print ("Lista vacia")
        
        print("Recorriendo de Fin a Inicio")
        actual = self.cola
        while actual:
            print(actual.dato, end =" -> ")
            actual = actual.anterior
        print("Fin")

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False
        
    def __len__(self):
        contador = 0
        actual = self.cabeza 
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"

        elementos = []
        actual = self.cabeza 
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <=> ".join(elementos)
    
lista = ListaDoble()
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
lista.insertar_inicio(40)
print(lista)
lista.recorrer_adelante()
lista.recorrer_atras()
print(f"Tamaño de la lista: {len(lista)} nodos")
print(lista.buscar(40))