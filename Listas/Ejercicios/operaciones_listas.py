"""
OPERACIONES COMPLEJAS EN LISTAS ENLAZADAS
----------------------------------------
Basado en el estilo de evaluación de AyP4.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None

class MiLista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, v):
        nuevo = Nodo(v)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    # 1. Mezclar dos listas ordenadas (Recursivo)
    def mezclar(self, otra_lista):
        self.cabeza = self._mezclar_rec(self.cabeza, otra_lista.cabeza)

    def _mezclar_rec(self, n1, n2):
        if n1 is None: return n2
        if n2 is None: return n1

        if n1.valor <= n2.valor:
            n1.sig = self._mezclar_rec(n1.sig, n2)
            return n1
        else:
            n2.sig = self._mezclar_rec(n1, n2.sig)
            return n2

    # 2. Particionar por valor X (menores a la izquierda, mayores a la derecha)
    def particionar(self, x):
        menores = MiLista()
        mayores = MiLista()
        self._part_rec(self.cabeza, x, menores, mayores)
        # Unir menores con mayores
        if menores.cabeza is None:
            self.cabeza = mayores.cabeza
            return
        
        actual = menores.cabeza
        while actual.sig:
            actual = actual.sig
        actual.sig = mayores.cabeza
        self.cabeza = menores.cabeza

    def _part_rec(self, nodo, x, menores, mayores):
        if nodo is None: return
        if nodo.valor < x:
            menores.agregar(nodo.valor)
        else:
            mayores.agregar(nodo.valor)
        self._part_rec(nodo.sig, x, menores, mayores)

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.sig
        print("None")

if __name__ == "__main__":
    l1 = MiLista()
    for v in [10, 8, 5, 2]: l1.agregar(v)
    l2 = MiLista()
    for v in [9, 7, 4, 1]: l2.agregar(v)
    
    print("Lista 1:", end=" ")
    l1.mostrar()
    print("Lista 2:", end=" ")
    l2.mostrar()
    
    l1.mezclar(l2)
    print("Mezcladas:", end=" ")
    l1.mostrar()
    
    l1.particionar(5)
    print("Particionada por 5:", end=" ")
    l1.mostrar()
