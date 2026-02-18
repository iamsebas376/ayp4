class NodoInventario:
    def __init__(self, nombre, es_categoria=True, precio=0):
        self.nombre = nombre
        self.es_categoria = es_categoria
        self.precio = precio
        self.hijos = [] # Solo si es_categoria es True

    def agregar_hijo(self, nodo):
        if self.es_categoria:
            self.hijos.append(nodo)

    # EJERCICIO 1: Calcular el valor total del inventario de una categoría
    def calcular_valor_total(self):
        if not self.es_categoria:
            return self.precio
        
        total = 0
        for hijo in self.hijos:
            total += hijo.calcular_valor_total()
        return total

    # EJERCICIO 2: Contar cuántos productos (no categorías) hay en total
    def contar_productos(self):
        if not self.es_categoria:
            return 1
        
        conteo = 0
        for hijo in self.hijos:
            conteo += hijo.contar_productos()
        return conteo

    # EJERCICIO 3: Buscar si un producto existe por nombre
    def buscar_producto(self, nombre_buscar):
        if self.nombre.lower() == nombre_buscar.lower() and not self.es_categoria:
            return True
        
        if self.es_categoria:
            for hijo in self.hijos:
                if hijo.buscar_producto(nombre_buscar):
                    return True
        return False

# Construcción de un Inventario
tienda = NodoInventario("Tienda Tech", True)

laptop_cat = NodoInventario("Laptops", True)
gamer_subcat = NodoInventario("Gaming", True)
gamer_subcat.agregar_hijo(NodoInventario("Asus ROG", False, 1500))
gamer_subcat.agregar_hijo(NodoInventario("MSI Stealth", False, 1800))

oficina_subcat = NodoInventario("Oficina", True)
oficina_subcat.agregar_hijo(NodoInventario("MacBook Air", False, 1000))

laptop_cat.agregar_hijo(gamer_subcat)
laptop_cat.agregar_hijo(oficina_subcat)

accesorios_cat = NodoInventario("Accesorios", True)
accesorios_cat.agregar_hijo(NodoInventario("Mouse Logitech", False, 50))
accesorios_cat.agregar_hijo(NodoInventario("Teclado Mecánico", False, 120))

tienda.agregar_hijo(laptop_cat)
tienda.agregar_hijo(accesorios_cat)

# Pruebas
print(f"Valor total del inventario: ${tienda.calcular_valor_total()}")
print(f"Número total de productos: {tienda.contar_productos()}")

producto = "MacBook Air"
if tienda.buscar_producto(producto):
    print(f"El producto '{producto}' está disponible.")
else:
    print(f"El producto '{producto}' no se encuentra.")
