# PRACTICA 2: GESTIÓN DE NOTIFICACIONES Y FEED (RED SOCIAL)
# TEMAS: REGEX EXTRACTION + DOUBLY LINKED LIST + INTERSECCIÓN SETS + RECURSIVIDAD DOBLE

import re

# 1. CLASE NODO (POST)
class Post:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto
        self.anterior = None
        self.siguiente = None

# 2. FEED DE ACTIVIDAD (DOUBLY LINKED LIST)
class FeedSocial:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def publicar(self, usuario, texto):
        nuevo = Post(usuario, texto)
        if not self.inicio:
            self.inicio = self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo
        return True

    def extraer_hashtags(self, texto):
        return set(re.findall(r"#(\w+)", texto.lower()))

    def extraer_menciones(self, texto):
        return set(re.findall(r"@(\w+)", texto.lower()))

    def buscar_mencion_rec(self, actual, user_objetivo):
        if actual is None:
            return None
        
        mencionados = self.extraer_menciones(actual.texto)
        if user_objetivo.lower() in mencionados:
            return actual
        
        return self.buscar_mencion_rec(actual.siguiente, user_objetivo)

    def temas_en_comun(self, post1, post2):
        tags1 = self.extraer_hashtags(post1.texto)
        tags2 = self.extraer_hashtags(post2.texto)
        return tags1 & tags2 

    def todos_los_hashtags_rec(self, actual):
        if actual is None:
            return set()
        
        tags_actual = self.extraer_hashtags(actual.texto)
        return tags_actual | self.todos_los_hashtags_rec(actual.siguiente)

if __name__ == "__main__":
    red = FeedSocial()
    red.publicar("Lucas", "Hoy estudiando #Estructuras y #Python con @Sofa")
    red.publicar("Sofa", "Me encanta #Python y #IA @Lucas #Divertido")
    
    encontrado = red.buscar_mencion_rec(red.inicio, "Sofa")
    if encontrado:
        print(f"Post encontrado: '{encontrado.texto}' de {encontrado.usuario}")
    
    comunes = red.temas_en_comun(red.inicio, red.inicio.siguiente)
    print(f"Temas en común: {comunes}")
    print(f"Todos los hashtags: {red.todos_los_hashtags_rec(red.inicio)}")
