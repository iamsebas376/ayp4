# PRACTICA 3: CONTROL DE INVENTARIO CIRCULAR
# TEMAS: LISTA CIRCULAR SIMPLE + SET DIFFERENCE + REGEX SKU + RECURSIVIDAD EN CIRCULARES

import re

# 1. CLASE NODO (PRODUCTO)
class Producto:
    def __init__(self, sku, nombre, cantidad):
        self.sku = sku # Formato: AAA-000
        self.nombre = nombre
        self.cantidad = cantidad
        self.siguiente = None

# 2. BODEGA (CIRCULAR LINKED LIST)
class Bodega:
    def __init__(self):
        self.ultimo = None
        self.skus_registrados = set()

    def agregar_producto(self, sku, nombre, cantidad):
        if not re.match(r"^[A-Z]{3}-\d{3}$", sku):
            print(f"Error: SKU '{sku}' no tiene formato.")
            return False
        
        nuevo = Producto(sku, nombre, cantidad)
        if not self.ultimo:
            self.ultimo = nuevo
            nuevo.siguiente = nuevo
        else:
            nuevo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        
        self.skus_registrados.add(sku)
        return True

    def sumar_stock_rec(self, actual, inicio=None):
        if not self.ultimo:
            return 0
        if inicio is None:
            inicio = self.ultimo.siguiente
        
        if actual.siguiente == inicio:
            return actual.cantidad
            
        return actual.cantidad + self.sumar_stock_rec(actual.siguiente, inicio)

    def detectar_faltantes(self, lista_skus_pedidos):
        pedidos_set = set(lista_skus_pedidos)
        return pedidos_set - self.skus_registrados

if __name__ == "__main__":
    bodega = Bodega()
    bodega.agregar_producto("ELE-101", "Laptop", 10)
    bodega.agregar_producto("ELE-202", "Mouse", 50)
    
    primer_nodo = bodega.ultimo.siguiente
    print(f"Total stock: {bodega.sumar_stock_rec(primer_nodo)}")
    
    pedido_cliente = ["ELE-101", "ELE-555"]
    print(f"Faltan en stock: {bodega.detectar_faltantes(pedido_cliente)}")
