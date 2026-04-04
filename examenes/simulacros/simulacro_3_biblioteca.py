"""
═══════════════════════════════════════════════════════════════════════════════
                    SIMULACRO PARCIAL 1 - MODELO 3
                     SISTEMA DE BIBLIOTECA DIGITAL
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
La Red Capital de Bibliotecas necesita sincronizar sus inventarios.
Debes usar CONJUNTOS (Sets) para las categorías y RECURSIVIDAD para los estantes.

REQUERIMIENTOS:
1. (1.0) Clase Libro: ISBN (Regex), Titulo, Categorias (Set).
2. (1.0) Clase Estante: Es un nodo de una LISTA ENLAZADA que contiene un Libro.
3. (1.5) Método RECURSIVO 'buscar_por_ISBN': Retorna el Libro si el ISBN coincide 
   con el patrón regex `^LIB-\d{4}-[A-Z]{2}$`.
4. (1.5) Operación entre Conjuntos: Implementa un método que reciba dos Estantes 
   (nodos) y retorne las categorías que AMBOS libros tienen en común.
"""

import re

class Libro:
    def __init__(self, isbn, titulo, categorias):
        self.isbn = isbn
        self.titulo = titulo
        self.categorias = set(categorias) # Conjunto de strings

class Estante:
    def __init__(self, libro):
        self.libro = libro
        self.siguiente = None

class Biblioteca:
    def __init__(self):
        self.cabeza = None

    def agregar_libro(self, libro):
        nuevo = Estante(libro)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def validar_isbn(self, isbn):
        patron = r"^LIB-\d{4}-[A-Z]{2}$"
        return bool(re.match(patron, isbn))

    def buscar_recursivo_isbn(self, nodo, isbn_objetivo):
        if nodo is None:
            return None
        
        if nodo.libro.isbn == isbn_objetivo:
            if self.validar_isbn(isbn_objetivo):
                return nodo.libro
            else:
                print("ISBN encontrado pero formato inválido.")
                return None
        
        return self.buscar_recursivo_isbn(nodo.siguiente, isbn_objetivo)

    def categorias_comunes_rec(self, n1, n2):
        """Retorna la intersección de categorías entre dos libros dados sus nodos."""
        if not n1 or not n2: return set()
        return n1.libro.categorias & n2.libro.categorias # Intersección de sets

    def mostrar_catalogo_rec(self, nodo):
        if nodo is None: return
        print(f"ISBN: {nodo.libro.isbn} | Título: {nodo.libro.titulo} | Categorías: {nodo.libro.categorias}")
        self.mostrar_catalogo_rec(nodo.siguiente)

if __name__ == "__main__":
    biblio = Biblioteca()
    
    # Crear libros
    l1 = Libro("LIB-1234-AB", "Cien Años de Soledad", ["Literatura", "Clásico"])
    l2 = Libro("LIB-5678-CD", "El Amor en los Tiempos del Cólera", ["Literatura", "Romance"])
    
    biblio.agregar_libro(l1)
    biblio.agregar_libro(l2)
    
    print("\n--- CATÁLOGO ---")
    biblio.mostrar_catalogo_rec(biblio.cabeza)
    
    # Prueba Intersección
    comunes = biblio.categorias_comunes_rec(biblio.cabeza, biblio.cabeza.siguiente)
    print(f"\nCategorías en común: {comunes}")
    
    # Prueba Búsqueda Regex
    isbn_test = "LIB-1234-AB"
    resultado = biblio.buscar_recursivo_isbn(biblio.cabeza, isbn_test)
    if resultado:
        print(f"\nLibro encontrado con ISBN válido: {resultado.titulo}")
