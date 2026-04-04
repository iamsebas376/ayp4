"""
═══════════════════════════════════════════════════════════════════════════════
                    SIMULACRO PARCIAL 1 - MODELO 5
                     CARRITO DE COMPRAS Y ENTREGAS (E-COMMERCE)
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
Un sistema de compras en línea necesita gestionar los carritos de los usuarios y 
la prioridad de los envíos para clientes VIP.
Debes usar una PILA (Stack) para el carrito y un HEAP para los envíos.

REQUERIMIENTOS:
1. (1.0) Clase Producto: Nombre, Precio, Puntero (`sig`).
2. (1.0) Pila Carrito: Implementa el método 'agregar' (Push) y 'deshacer_ultimo' (Pop).
3. (1.5) Método RECURSIVO 'total_pagar': Recorre la pila del carrito y retorna la suma de precios.
4. (1.5) Fila de Envíos VIP: Usa un HEAP para gestionar pedidos de entrega, 
   donde la prioridad es el tiempo de suscripción del usuario (años).
"""

import heapq

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.siguiente = None

class Carrito:
    def __init__(self):
        self.tope = None

    def agregar_producto(self, nombre, precio):
        nuevo = Producto(nombre, precio)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def deshacer_ultimo(self):
        if self.tope:
            eliminado = self.tope
            self.tope = self.tope.siguiente
            return eliminado
        return None

    def calcular_total_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.precio + self.calcular_total_rec(nodo.siguiente)

class Logistica:
    def __init__(self):
        self.envios_prioritarios = [] # Heap

    def registrar_envio(self, usuario, anios_vip, productos):
        # En el heap guardamos (prioridad, data)
        # En Python el menor número sale primero, usamos -anios para que el
        # mayor tiempo sea el de mayor prioridad (más negativo).
        heapq.heappush(self.envios_prioritarios, (-anios_vip, usuario, productos))

    def despachar_siguiente(self):
        if self.envios_prioritarios:
            prio, user, prods = heapq.heappop(self.envios_prioritarios)
            print(f"Despachando pedido para: {user} (VIP {abs(prio)} años)")
            return True
        return False

if __name__ == "__main__":
    mi_carrito = Carrito()
    mi_carrito.agregar_producto("Laptop", 1200)
    mi_carrito.agregar_producto("Mouse", 25)
    mi_carrito.agregar_producto("Teclado", 50)
    
    total = mi_carrito.calcular_total_rec(mi_carrito.tope)
    print(f"\n--- CARRITO ---")
    print(f"Total a pagar: ${total}")
    
    print("\nEliminando último producto (Pop)...")
    mi_carrito.deshacer_ultimo()
    nuevo_total = mi_carrito.calcular_total_rec(mi_carrito.tope)
    print(f"Nuevo total: ${nuevo_total}")
    
    print("\n--- LOGÍSTICA (HEAP) ---")
    envios = Logistica()
    envios.registrar_envio("Pedro", 2, ["Mouse"])
    envios.registrar_envio("Maria", 10, ["Laptop"])
    envios.registrar_envio("Juan", 5, ["Teclado"])
    
    envios.despachar_siguiente()
    envios.despachar_siguiente()
