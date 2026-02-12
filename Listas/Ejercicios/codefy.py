# Aplicación que simule plataformas tipo Spotify con listas, donde:
# 1. [X] Interfaz de usuario simple por consola
# 2. [X] Menú interactivo para seleccionar acciones
# 3. [ ] Agregar canciones en cualquier parte de la lista
# 3. [X] Eliminar canciones en cualquier parte de la lista
# 4. [ ] Validar datos al agregar canciones (campos obligatorios, tipos)
# 5. [ ] Permitir editar información de una canción
# 6. [X] Mostrar todas las canciones en formato de lista
# 7. [X] Implementar buscador de canciones
# 8. [ ] Reproducir canción por diferentes criterios (por nombre, género, artista, álbum, año, siguiente, anterior, última, primera)
# 9. [X] Mostrar duración de la canción1
# 10. [ ] Agregar modo aleatorio de reproducción
# 11. [ ] Agregar opción de repetir lista
# 12. [ ] Guardar y cargar la lista de canciones desde archivo
# 13. [ ] Siguiente y anterior canción
# 14. [ ] Duración total de la lista
# 15. [ ] Cantidad de canciones en la lista


class Cancion:
    def __init__(self, nombre, artista, genero, album, anio, duracion):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.album = album
        self.anio = anio
        self.duracion = duracion

    def __str__(self):
        return f"{self.nombre} - {self.artista} ({self.anio}) [{self.genero}] | {self.album} | {self.duracion}"

class Node:
    def __init__(self, cancion):
        self.dato = cancion
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None
        self.cola = None
        self.actual = None
        self._cantidad = 0

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_cancion(self, cancion):
        nuevo = Node(cancion)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self._cantidad += 1

    def eliminar_por_nombre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        self._cantidad -= 1
        return False

    def buscar(self, nombre):
        while self.actual:
            if self.actual.dato.nombre.lower() == nombre.lower():
                return self.actual.dato
            self.actual = self.actual.siguiente
        return None

    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "\n".join(elementos)

class Reproductor:
    def __initi__(self):
        self.lista_canciones = ListaDoble()
        self.cancion_actual = None
        self.modo_aleatorio = False
        self.repetir_lista = False

class InterfazConsola:
    def __init__(self, lista):
        self.lista = lista

    def mostrar_menu(self):
        print("\n--- CODEFY ---")
        print("1. Mostrar canciones")
        print("2. Agregar canción")
        print("3. Eliminar canción")
        print("4. Buscar canción")
        print("5. Salir")

    def pedir_datos_cancion(self):
        nombre = input("Nombre: ")
        artista = input("Artista: ")
        genero = input("Género: ")
        album = input("Álbum: ")
        anio = input("Año: ")
        duracion = input("Duración (mm:ss): ")
        return Cancion(nombre, artista, genero, album, anio, duracion)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                print("\nLista de canciones:")
                print(self.lista)

            elif opcion == "2":
                cancion = self.pedir_datos_cancion()
                self.lista.insertar_final(cancion)
                print("Canción agregada.")

            elif opcion == "3":
                nombre = input("Nombre de la canción a eliminar: ")
                self.lista.eliminar_por_nombre(nombre)
                print("Canción eliminada.")

            elif opcion == "4":
                nombre = input("Nombre de la canción a buscar: ")
                cancion = self.lista.buscar(nombre)
                if cancion:
                    print("Encontrada:", cancion)
                else:
                    print("No se encontró la canción.")

            elif opcion == "5":
                print("Hasta luego, gracias por usar Codefy!")
                break

            else:
                print("Opción no válida.")

lista_canciones = ListaDoble()
lista_canciones.agregar_cancion(Cancion("Imagine", "John Lennon", "Rock", "Imagine", 1971, "3:04"))
lista_canciones.agregar_cancion(Cancion("Yesterday", "The Beatles", "Pop", "Help!", 1965, "2:05"))
lista_canciones.agregar_cancion(Cancion("Bohemian Rhapsody", "Queen", "Rock", "A Night at the Opera", 1975, "5:55"))
lista_canciones.agregar_cancion(Cancion("Billie Jean", "Michael Jackson", "Pop", "Thriller", 1982, "4:54"))

if __name__ == "__main__":
    InterfazConsola(lista_canciones).ejecutar()