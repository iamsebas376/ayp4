"""
═══════════════════════════════════════════════════════════════════════════════
                    SIMULACRO PARCIAL 1 - MODELO 2
                     SISTEMA DE CONTROL DE TRÁFICO AÉREO
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
El aeropuerto "El Dorado" necesita gestionar los vuelos que esperan pista. 
Debes usar una LISTA CIRCULAR SIMPLE para los vuelos comerciales y un HEAP para 
vuelos de emergencia.

REQUERIMIENTOS:
1. (1.0) Clase Vuelo: codigo (string), combustible (%), tipo ("Comercial" o "Emergencia").
2. (1.0) Lista Circular: Implementa el método 'agregar_vuelo' para los comerciales.
3. (1.5) Método RECURSIVO 'atención_prioridad': Recorre la lista circular y retorna 
   el primer vuelo con combustible < 15%.
4. (1.5) Heap de Emergencias: Implementa una función que reciba una lista de vuelos 
   de emergencia y los atienda usando `heapq`, donde la prioridad es el nivel 
   de combustible (menor combustible = mayor prioridad).
"""

import heapq

class Vuelo:
    def __init__(self, codigo, combustible, tipo="Comercial"):
        self.codigo = codigo
        self.combustible = combustible
        self.tipo = tipo
        self.siguiente = None

class ControlAereo:
    def __init__(self):
        self.ultimo = None
        self.emergencias = [] # Heap

    def agregar_vuelo_comercial(self, codigo, combustible):
        nuevo = Vuelo(codigo, combustible)
        if not self.ultimo:
            self.ultimo = nuevo
            nuevo.siguiente = nuevo
        else:
            nuevo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def agregar_vuelo_emergencia(self, codigo, combustible):
        # En el heap guardamos (prioridad, objeto)
        # Menor combustible sale primero
        heapq.heappush(self.emergencias, (combustible, codigo))

    def buscar_emergencia_critica_rec(self, actual, inicio=None):
        """Busca recursivamente en la lista circular un vuelo comercial crítico."""
        if not self.ultimo: return None
        if not inicio: inicio = self.ultimo.siguiente
        
        # Caso base: si el siguiente vuelve a ser el inicio, termina
        if actual.siguiente == inicio and actual.combustible >= 15:
            return None
        
        if actual.combustible < 15:
            return actual
        
        return self.buscar_emergencia_critica_rec(actual.siguiente, inicio)

    def atender_emergencias(self):
        print("\n--- ATENDIENDO EMERGENCIAS (HEAP) ---")
        while self.emergencias:
            comb, cod = heapq.heappop(self.emergencias)
            print(f"Pista libre para: {cod} (Combustible: {comb}%)")

if __name__ == "__main__":
    torre = ControlAereo()
    
    # Agregar comerciales
    torre.agregar_vuelo_comercial("AV123", 40)
    torre.agregar_vuelo_comercial("LA456", 12) # CRÍTICO
    torre.agregar_vuelo_comercial("IB789", 30)
    
    critico = torre.buscar_emergencia_critica_rec(torre.ultimo.siguiente)
    if critico:
        print(f"Vuelo comercial crítico detectado: {critico.codigo}")
    
    # Agregar emergencias al heap
    torre.agregar_vuelo_emergencia("MAYDAY-1", 5)
    torre.agregar_vuelo_emergencia("MAYDAY-2", 10)
    torre.atender_emergencias()
