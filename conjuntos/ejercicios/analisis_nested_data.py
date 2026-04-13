"""
EJERCICIO NIVEL EXAMEN: Limpieza de Datos Anidados
Contexto: Recibes una lista de productos de una API, pero vienen duplicados 
y con diferentes formatos. Debes extraer las categorías ÚNICAS.
"""

data_cruda = [
    {"id": 1, "nombre": "Laptop", "categorias": ["Electrónica", "Computación"]},
    {"id": 2, "nombre": "Mouse", "categorias": ["Electrónica", "Periféricos"]},
    {"id": 3, "nombre": "Monitor", "categorias": ["Electrónica", "Computación"]},
    {"id": 4, "nombre": "Teclado", "categorias": ["Periféricos", "Accesorios"]},
]

def extraer_categorias_unicas(datos):
    categorias_totales = set()
    
    for producto in datos:
        # Convertimos la lista de categorías del producto en un conjunto
        categorias_producto = set(producto["categorias"])
        
        # Unión con el conjunto global
        categorias_totales |= categorias_producto
        
    return categorias_totales

resultado = extraer_categorias_unicas(data_cruda)
print(f"Categorías únicas encontradas: {resultado}")
print(f"Total de categorías: {len(resultado)}")
