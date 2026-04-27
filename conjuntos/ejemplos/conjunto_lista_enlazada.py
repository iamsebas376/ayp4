class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class ConjuntoEnlazado:
    """
    Implementación de un Conjunto utilizando una Lista Simplemente Enlazada.
    Un conjunto no permite elementos duplicados.
    """
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def es_vacio(self):
        return self.cabeza is None

    def contiene(self, dato):
        """Verifica si un elemento ya existe en el conjunto."""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, dato):
        """Agrega un elemento si no existe previamente (Propiedad de Conjunto)."""
        if not self.contiene(dato):
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            self.tamano += 1
            return True
        return False

    def eliminar(self, dato):
        """Elimina un elemento del conjunto."""
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def union(self, otro_conjunto):
        """Retorna un nuevo conjunto con elementos de ambos."""
        resultado = ConjuntoEnlazado()
        
        # Agregar elementos del primer conjunto
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
            
        # Agregar elementos del segundo conjunto
        actual = otro_conjunto.cabeza
        while actual:
            resultado.agregar(actual.dato) # agregar() ya valida duplicados
            actual = actual.siguiente
            
        return resultado

    def interseccion(self, otro_conjunto):
        """Retorna un nuevo conjunto con elementos comunes."""
        resultado = ConjuntoEnlazado()
        actual = self.cabeza
        while actual:
            if otro_conjunto.contiene(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia(self, otro_conjunto):
        """Retorna un nuevo conjunto con elementos de A que no están en B (A - B)."""
        resultado = ConjuntoEnlazado()
        actual = self.cabeza
        while actual:
            if not otro_conjunto.contiene(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"

# Ejemplo de uso
if __name__ == "__main__":
    A = ConjuntoEnlazado()
    B = ConjuntoEnlazado()

    for x in [1, 2, 3, 4, 5]: A.agregar(x)
    for x in [4, 5, 6, 7, 8]: B.agregar(x)

    print(f"Conjunto A: {A}")
    print(f"Conjunto B: {B}")
    print(f"Unión: {A.union(B)}")
    print(f"Intersección: {A.interseccion(B)}")
    print(f"Diferencia (A - B): {A.diferencia(B)}")
