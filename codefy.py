# Aplicación que simule plataformas de spotify con listas, donde:
# - Pueda agregar o eliminar canciones en cualquier parte de la lista
# - Pueda reproducir la canción que quiera (Por nombre, genero, artista, albúm, año, siguiente, anterior, última, primera)
# - Tenga buscador de canciones
# - Duración de la canción
# - Modo aleatorio
# - Repetir lista

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
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nodoNuevo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nodoNuevo
            self.cola = nodoNuevo
        else:
            nodoNuevo.siguiente = self.cabeza
            self.cabeza.anterior = nodoNuevo
            self.cabeza = nodoNuevo

    def insertar_final(self, dato):
        nodoNuevo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nodoNuevo
            self.cola = nodoNuevo
        else:
            self.cola.siguiente = nodoNuevo
            nodoNuevo.anterior = self.cola
            self.cola = nodoNuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    def eliminar_final(self):
        if self.esta_vacia():
            return None

        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    def eliminar_especifico(self, dato):
        if self.esta_vacia():
            return None

    def recorrer_adelante(self):
        if self.esta_vacia():
            return "Lista vacia"
        
        print("Recorriendo de Inicio a Fin")
        actual = self.cabeza
        while actual:
            print(actual.dato, end =" -> ")
            actual = actual.siguiente
        print("Fin")

    def recorrer_atras(self):
        if self.esta_vacia():
            return print ("Lista vacia")
        
        print("Recorriendo de Fin a Inicio")
        actual = self.cola
        while actual:
            print(actual.dato, end =" -> ")
            actual = actual.anterior
        print("Fin")

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False
        
    def __len__(self):
        contador = 0
        actual = self.cabeza 
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"

        elementos = []
        actual = self.cabeza 
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "\n".join(elementos)

lista_canciones = ListaDoble()
lista_canciones.insertar_final(Cancion("Imagine", "John Lennon", "Rock", "Imagine", 1971, "3:04"))
lista_canciones.insertar_final(Cancion("Yesterday", "The Beatles", "Pop", "Help!", 1965, "2:05"))
lista_canciones.insertar_final(Cancion("Bohemian Rhapsody", "Queen", "Rock", "A Night at the Opera", 1975, "5:55"))
lista_canciones.insertar_final(Cancion("Billie Jean", "Michael Jackson", "Pop", "Thriller", 1982, "4:54"))

print(lista_canciones)