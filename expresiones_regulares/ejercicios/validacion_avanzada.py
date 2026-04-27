"""
EJERCICIOS DE EXPRESIONES REGULARES (REGEX)
------------------------------------------
Validación de datos comunes en sistemas reales.
"""

import re

# 1. EJERCICIO: Validar Tarjeta de Crédito (16 dígitos, 4-4-4-4 o 16 seguidos)
def validar_tarjeta(t):
    # Formatos: 1234-5678-9012-3456 o 1234567890123456
    patron = r"^\d{4}(-?\d{4}){3}$"
    return bool(re.match(patron, t))

# 2. EJERCICIO: Extraer Fechas (DD/MM/AAAA) de un texto
def extraer_fechas(texto):
    # Dia: 01-31, Mes: 01-12, Año: 4 dígitos
    patron = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"
    return re.findall(patron, texto)

# 3. EJERCICIO: Validar Contraseña Fuerte
def validar_password(p):
    """
    Criterios:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos un número
    - Al menos un caracter especial (@$!%*?&)
    """
    patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(patron, p))

# 4. EJERCICIO: Validar Placa Colombiana (AAA123 o AAA12C para motos)
def validar_placa(placa):
    # Carros: 3 letras + 3 números
    # Motos: 3 letras + 2 números + 1 letra
    patron = r"^[A-Z]{3}\d{2}[A-Z\d]$"
    return bool(re.match(patron, placa))


if __name__ == "__main__":
    print(f"Tarjeta '1234-5678-9012-3456' válida: {validar_tarjeta('1234-5678-9012-3456')}")
    print(f"Tarjeta '12345678' válida: {validar_tarjeta('12345678')}")
    
    texto = "Hoy es 04/04/2026 y el parcial es el 15/04/2026."
    print(f"Fechas encontradas: {extraer_fechas(texto)}")
    
    print(f"Password 'Pass123!' válida: {validar_password('Pass123!')}")
    print(f"Password 'pass123' válida: {validar_password('pass123')}")
    
    print(f"Placa 'ABC123' válida: {validar_placa('ABC123')}")
    print(f"Placa 'ABC12D' válida: {validar_placa('ABC12D')}")
