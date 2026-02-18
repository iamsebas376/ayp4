import os

class Archivo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = []

    def agregar(self, item):
        self.contenido.append(item)

    # 1. EJERCICIO: Calcular el tamaño total de la carpeta (incluyendo subcarpetas)
    def calcular_tamano_total(self):
        return self._calcular_tamano_total_rec(self)

    def _calcular_tamano_total_rec(self, item):
        if isinstance(item, Archivo):
            return item.tamano
        
        total = 0
        for subitem in item.contenido:
            total += self._calcular_tamano_total_rec(subitem)
        return total

    # 2. EJERCICIO: Buscar un archivo por nombre y devolver su tamaño
    def buscar_archivo(self, nombre_buscar):
        return self._buscar_archivo_rec(self, nombre_buscar)

    def _buscar_archivo_rec(self, item, nombre_buscar):
        if isinstance(item, Archivo):
            if item.nombre == nombre_buscar:
                return item.tamano
            return None
        
        for subitem in item.contenido:
            resultado = self._buscar_archivo_rec(subitem, nombre_buscar)
            if resultado is not None:
                return resultado
        return None

    # 3. EJERCICIO: Listar todo el contenido con indentación para mostrar la jerarquía
    def listar_contenido(self, nivel=0):
        print("  " * nivel + "|-- " + self.nombre + " (Carpeta)")
        for item in self.contenido:
            if isinstance(item, Archivo):
                print("  " * (nivel + 1) + "|-- " + item.nombre + f" ({item.tamano} KB)")
            else:
                item.listar_contenido(nivel + 1)

# Simulación de un sistema de archivos
root = Carpeta("C:")
user = Carpeta("Usuarios")
docs = Carpeta("Documentos")
imgs = Carpeta("Imagenes")

root.agregar(user)
user.agregar(docs)
user.agregar(imgs)

docs.agregar(Archivo("tarea.docx", 50))
docs.agregar(Archivo("planificador.xlsx", 120))

sub_docs = Carpeta("Universidad")
docs.agregar(sub_docs)
sub_docs.agregar(Archivo("proyecto_final.pdf", 500))

imgs.agregar(Archivo("foto_perfil.png", 200))
imgs.agregar(Archivo("vacaciones.jpg", 1500))

# Casos de prueba
print("--- Jerarquía del Sistema de Archivos ---")
root.listar_contenido()

print(f"\nTamaño total de la unidad C: {root.calcular_tamano_total()} KB")

nombre = "proyecto_final.pdf"
tam = root.buscar_archivo(nombre)
if tam:
    print(f"\nArchivo found: {nombre} ocupa {tam} KB")
else:
    print(f"\nArchivo {nombre} no encontrado")
