class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # 1. Recorrido / Impresión
    def imprimir(self):
        print("Lista:", end=" ")
        self._imprimir_rec(self.cabeza)
        print("None")

    def _imprimir_rec(self, nodo):
        if nodo is None:
            return
        print(f"[{nodo.valor}] ->", end=" ")
        self._imprimir_rec(nodo.siguiente)

    # 2. Conteo de Nodos
    def contar(self):
        return self._contar_rec(self.cabeza)

    def _contar_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_rec(nodo.siguiente)

    # 3. Suma de Valores (si son numéricos)
    def sumar(self):
        return self._sumar_rec(self.cabeza)

    def _sumar_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.valor + self._sumar_rec(nodo.siguiente)

    # 4. Buscar un Valor (Retorna True/False)
    def buscar(self, objetivo):
        return self._buscar_rec(self.cabeza, objetivo)

    def _buscar_rec(self, nodo, objetivo):
        if nodo is None:
            return False
        if nodo.valor == objetivo:
            return True
        return self._buscar_rec(nodo.siguiente, objetivo)

    # 5. Encontrar el Valor Máximo
    def encontrar_maximo(self):
        if not self.cabeza:
            return None
        return self._maximo_rec(self.cabeza, self.cabeza.valor)

    def _maximo_rec(self, nodo, actual_max):
        if nodo is None:
            return actual_max
        if nodo.valor > actual_max:
            actual_max = nodo.valor
        return self._maximo_rec(nodo.siguiente, actual_max)

    # 6. Invertir la Lista (Retorna la nueva cabeza)
    def invertir(self):
        self.cabeza = self._invertir_rec(self.cabeza)

    def _invertir_rec(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return nodo
        nueva_cabeza = self._invertir_rec(nodo.siguiente)
        nodo.siguiente.siguiente = nodo
        nodo.siguiente = None
        return nueva_cabeza

    # 7. Eliminar un Nodo por Valor
    def eliminar(self, valor):
        self.cabeza = self._eliminar_rec(self.cabeza, valor)

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.valor == valor:
            return nodo.siguiente # Saltamos el nodo actual
        nodo.siguiente = self._eliminar_rec(nodo.siguiente, valor)
        return nodo

lista = ListaEnlazada()
elementos = [10, 25, 5, 40, 15]

for e in elementos:
    lista.agregar(e)

print(f"--- Operaciones Recursivas sobre Nodos ---")
lista.imprimir()
print(f"Total de nodos: {lista.contar()}")
print(f"Suma de valores: {lista.sumar()}")
print(f"¿Existe el 40?: {lista.buscar(40)}")
print(f"¿Existe el 100?: {lista.buscar(100)}")
print(f"Valor máximo: {lista.encontrar_maximo()}")

print("\nEliminando el 5...")
lista.eliminar(5)
lista.imprimir()

print("\nInvirtiendo la lista...")
lista.invertir()
lista.imprimir()
