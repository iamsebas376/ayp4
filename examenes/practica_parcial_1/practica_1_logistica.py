# PRACTICA 1: SISTEMA DE LOGÍSTICA DE PAQUETES
# TEMAS: REGEX + STACK (LISTA ENLAZADA) + SETS + RECURSIVIDAD CON MEMORIZACIÓN

import re

# 1. CLASE NODO (PAQUETE)
class Paquete:
    def __init__(self, tracking_id, ciudad, peso):
        self.tracking_id = tracking_id  # Formato: PKG-2024-A12
        self.ciudad = ciudad
        self.peso = peso
        self.siguiente = None

# 2. SISTEMA DE GESTIÓN (STACK)
class SistemaLogistica:
    def __init__(self):
        self.tope = None
        self.ciudades_unicas = set()
        self.cache_costos = {}

    def validar_tracking(self, tid):
        patron = r"^PKG-\d{4}-[A-Z\d]{3}$"
        return bool(re.match(patron, tid))

    def apilar_paquete(self, tid, ciudad, peso):
        if not self.validar_tracking(tid):
            print(f"Error: Tracking ID '{tid}' no es válido.")
            return False
        
        nuevo = Paquete(tid, ciudad, peso)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.ciudades_unicas.add(ciudad.lower())
        return True

    def contar_pesados_rec(self, actual, limite):
        if actual is None:
            return 0
        conteo = 1 if actual.peso > limite else 0
        return conteo + self.contar_pesados_rec(actual.siguiente, limite)

    def calcular_costo_complejo_memo(self, peso_entero):
        if peso_entero <= 1:
            return 10
        
        if peso_entero in self.cache_costos:
            return self.cache_costos[peso_entero]
        
        resultado = self.calcular_costo_complejo_memo(peso_entero - 1) + self.calcular_costo_complejo_memo(peso_entero - 2) + 5
        self.cache_costos[peso_entero] = resultado
        return resultado

    def obtener_ciudades_sin_entrega(self, ciudades_esperadas):
        return ciudades_esperadas - self.ciudades_unicas

if __name__ == "__main__":
    log = SistemaLogistica()
    log.apilar_paquete("PKG-2024-ABC", "Bogota", 10)
    log.apilar_paquete("PKG-2024-123", "Medellin", 25)
    
    print(f"Ciudades registradas (Set): {log.ciudades_unicas}")
    print(f"Paquetes > 15kg: {log.contar_pesados_rec(log.tope, 15)}")
    print(f"Costo para 30kg (Memo): {log.calcular_costo_complejo_memo(30)}")
