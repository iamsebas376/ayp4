"""
═══════════════════════════════════════════════════════════════════════════════
                    SIMULACRO PARCIAL 1 - MODELO 4
                     FEED DE NOTICIAS DE RED SOCIAL
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
Una micro-red social (tipo Twitter) necesita gestionar los posts de un muro.
Debes usar una LISTA DOBLEMENTE ENLAZADA para navegar adelante y atrás.

REQUERIMIENTOS:
1. (1.0) Clase Post: Usuario, Texto, Timestamps y Punteros (`sig`, `ant`).
2. (1.0) Método 'publicar': Agrega el nuevo post al INICIO (más reciente).
3. (1.5) Métodos 'siguiente' y 'anterior': Mueve un puntero `actual` por el feed.
4. (1.5) RECURSIVIDAD + REGEX: Implementa un método que recorra el feed y extraiga 
   todos los HASHTAGS (palabras que empiezan con #) usando `re.findall`.
"""

import re

class Post:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto
        self.siguiente = None
        self.anterior = None

class Feed:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def publicar(self, usuario, texto):
        nuevo = Post(usuario, texto)
        if not self.cabeza:
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            self.actual = nuevo

    def obtener_hashtags_rec(self, nodo):
        """Retorna una lista con todos los hashtags de todos los posts."""
        if nodo is None:
            return []
        
        # Encontrar hashtags en el texto del post actual
        hashtags = re.findall(r"#\w+", nodo.texto)
        
        # Llamada recursiva para el resto de la lista
        return hashtags + self.obtener_hashtags_rec(nodo.siguiente)

    def navegar_adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual
        return None

    def navegar_atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual
        return None

if __name__ == "__main__":
    feed = Feed()
    
    # Publicar posts
    feed.publicar("Sebas", "Hola mundo! #Coder #Python")
    feed.publicar("User2", "Estudiando para el parcial #AyP4 #Estructuras")
    feed.publicar("Admin", "Bienvenidos a la red social #Antigravity")
    
    print("\n--- EXTRAYENDO HASHTAGS RECURSIVAMENTE ---")
    lista_tags = feed.obtener_hashtags_rec(feed.cabeza)
    print(f"Hashtags encontrados: {lista_tags}")
    
    print("\n--- NAVEGANDO POR EL FEED ---")
    print(f"Estado Inicial (Actual): {feed.actual.texto}")
    
    proximo = feed.navegar_adelante()
    if proximo:
        print(f"Adelante -> {proximo.texto}")
    
    atras = feed.navegar_atras()
    if atras:
        print(f"Atrás -> {atras.texto}")
