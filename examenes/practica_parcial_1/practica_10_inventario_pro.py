# PRACTICA 10: EL "FINAL BOSS" (MERGESORT EN LISTA ENLAZADA)
# TEMAS: RECURSIVIDAD MÁXIMA (Divide y Vencerás) + LISTA ENLAZADA SIMPLE

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ProLista:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    # 1. Encontrar el punto medio recursivamente (Fast & Slow pointers)
    def obtener_medio_rec(self, cabeza):
        if cabeza is None: return cabeza
        
        lento = cabeza
        rapido = cabeza
        
        while rapido.siguiente and rapido.siguiente.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
            
        return lento

    # 2. Mezclar dos listas ordenadas recursivamente
    def mezclar_rec(self, h1, h2):
        if h1 is None: return h2
        if h2 is None: return h1
        
        if h1.valor <= h2.valor:
            resultado = h1
            resultado.siguiente = self.mezclar_rec(h1.siguiente, h2)
        else:
            resultado = h2
            resultado.siguiente = self.mezclar_rec(h1, h2.siguiente)
            
        return resultado

    # 3. Función MergeSort principal recursiva
    def merge_sort_rec(self, h):
        # Caso Base: si la lista está vacía o tiene un solo nodo
        if h is None or h.siguiente is None:
            return h
        
        # Obtener el medio y dividir la lista
        medio = self.obtener_medio_rec(h)
        siguiente_del_medio = medio.siguiente
        medio.siguiente = None # Cortar la lista en dos
        
        # Llamar recursivamente para cada mitad
        izquierda = self.merge_sort_rec(h)
        derecha = self.merge_sort_rec(siguiente_del_medio)
        
        # Mezclar las dos mitades ordenadas
        lista_ordenada = self.mezclar_rec(izquierda, derecha)
        return lista_ordenada

    def ordenar(self):
        self.cabeza = self.merge_sort_rec(self.cabeza)

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"[{actual.valor}] ", end="-> ")
            actual = actual.siguiente
        print("None")

if __name__ == "__main__":
    p = ProLista()
    import random
    
    # Generar lista desordenada
    nums = [15, 3, 22, 1, 9, 14, 5]
    for n in nums: p.agregar_al_final(n)
    
    print("\n--- Lista Original ---")
    p.mostrar()
    
    print("\n--- Ordenando con MergeSort Recursivo ---")
    p.ordenar()
    p.mostrar()
