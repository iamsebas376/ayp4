# PRACTICA 4: CALCULADORA FINANCIERA (COMBINACIONES Y PAGOS)
# TEMAS: RECURSIVIDAD COMPLEJA + MEMORIZACIÓN (CACHE) + REGEX CURRENCY

import re

# 1. CALCULADORA DE COMBINACIONES (MEMOIZACION)
class CalculadoraFinanciera:
    def __init__(self):
        self.cache_vias = {}
        self.cache_inversion = {}

    def formas_pagar_memo(self, monto, denominaciones, indice=0):
        if monto == 0: return 1
        if monto < 0 or indice >= len(denominaciones): return 0
        
        llave = (monto, indice)
        if llave in self.cache_vias:
            return self.cache_vias[llave]
        
        resultado = (self.formas_pagar_memo(monto - denominaciones[indice], denominaciones, indice) + 
                    self.formas_pagar_memo(monto, denominaciones, indice + 1))
        
        self.cache_vias[llave] = resultado
        return resultado

    def inversion_futura_memo(self, principal, tasa, tiempo):
        if tiempo == 0: return principal
        
        if tiempo in self.cache_inversion:
            return self.cache_inversion[tiempo]
        
        resultado = self.inversion_futura_memo(principal, tasa, tiempo - 1) * (1 + tasa)
        self.cache_inversion[tiempo] = resultado
        return resultado

    def validar_moneda(self, valor):
        patron = r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$"
        return bool(re.match(patron, valor))

if __name__ == "__main__":
    calc = CalculadoraFinanciera()
    monedas = [1, 2, 5]
    print(f"Formas $10: {calc.formas_pagar_memo(10, monedas)}")
    print(f"Inversión tras 10 años: ${calc.inversion_futura_memo(1000, 0.10, 10):.2f}")
    print(f"¿$1,234.56 es válido?: {calc.validar_moneda('$1,234.56')}")
