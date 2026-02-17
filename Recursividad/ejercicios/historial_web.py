class Web:
    def __init__(self, url):
        self.url = url
        self.siguiente = None

class Historial:
    def __init__(self):
        self.cabeza = None

    def agregar_pagina(self, url):
        nueva_pagina = Web(url)
        nueva_pagina.siguiente = self.cabeza
        self.cabeza = nueva_pagina

    def mostrar_historial(self):
        return self._mostrar_historial(self.cabeza)

    def _mostrar_historial(self, node, n=1):
        if node is None:
            return
        print(f"URL #{n}: {node.url}")
        return self._mostrar_historial(node.siguiente, n + 1)

    def contar_paginas(self):
        return self._contar_paginas(self.cabeza)

    def _contar_paginas(self, node):
        if node is None:
            return 0
        return 1 + self._contar_paginas(node.siguiente)

    def buscar_pagina(self, url):
        return self._buscar_pagina(self.cabeza, url)

    def _buscar_pagina(self, node, url):
        if node is None:
            return False
        if node.url == url:
            return True
        return self._buscar_pagina(node.siguiente, url)


web = Historial()
web.agregar_pagina("www.google.com")
web.agregar_pagina("www.amazon.com")
web.agregar_pagina("ww.apple.com")
web.agregar_pagina("www.elpoli.com")

while True:
    opcion = int(input("\nMENU \n 1. Agregar página \n 2. Mostrar total de paginas en el historial. \n 3. Buscar página. \n 4. Mostrar todas las paginas visitadas. \nOpción: "))
    if opcion == 1:
        pagina = input("Ingrese la página que quiere ingresar: ")
        web.agregar_pagina(pagina)
    if opcion == 2:
        print("\nNúmero total de URLs:", web.contar_paginas())
    if opcion == 3:
        pagina = input("Ingrese la página que quiere buscar: ")
        if web.buscar_pagina(pagina):
            print("La página se encuentra en el historial.")
        else:
            print("La página no se encuentra en el historial.")
    if opcion == 4:
        print(web.mostrar_historial())
    if opcion == 0:
        break
