# PRACTICA 7: DISTANCIA DE EDICIÓN (SIMILITUD DE TEXTO)
# TEMAS: RECURSIVIDAD COMPLEJA + MEMORIZACIÓN (CACHE) + COMPRESIÓN DE LISTAS

class ComparadorTextos:
    def __init__(self):
        self.memo = {}

    def distancia_edit(self, s1, s2):
        """Mínimo número de operaciones (insertar, borrar, cambiar) para transformar s1 en s2."""
        # Llave para caché: (longitud1, longitud2)
        llave = (len(s1), len(s2))
        
        if llave in self.memo:
            return self.memo[llave]
        
        # Caso base 1: Si s1 está vacío, insertar todos los de s2
        if not s1: return len(s2)
        
        # Caso base 2: Si s2 está vacío, borrar todos los de s1
        if not s2: return len(s1)
        
        # Si el último caracter es igual, no cuenta operación
        if s1[-1] == s2[-1]:
            resultado = self.distancia_edit(s1[:-1], s2[:-1])
        else:
            # Si no: probar 3 caminos y elegir el mínimo
            insert = self.distancia_edit(s1, s2[:-1])
            delete = self.distancia_edit(s1[:-1], s2)
            replace = self.distancia_edit(s1[:-1], s2[:-1])
            resultado = 1 + min(insert, delete, replace)
            
        self.memo[llave] = resultado
        return resultado

if __name__ == "__main__":
    c = ComparadorTextos()
    
    # Ejemplo 1: Palabra corta
    print(f"Distancia 'casa' a 'cama': {c.distancia_edit('casa', 'cama')}") # Output: 1 (cambiar s->m)
    
    # Ejemplo 2: Palabra larga (la memo es CRÍTICA aquí)
    print(f"Distancia 'universidad' a 'diversidad': {c.distancia_edit('universidad', 'diversidad')}") # Output: 3 (quitar u, n, i)
    print(f"Número de estados en caché: {len(c.memo)}")
