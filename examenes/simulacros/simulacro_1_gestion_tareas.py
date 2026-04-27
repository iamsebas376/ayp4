"""
═══════════════════════════════════════════════════════════════════════════════
                    SIMULACRO PARCIAL 1 - MODELO A 
                     SISTEMA DE GESTIÓN DE TAREAS
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
Un equipo de desarrollo ágil necesita organizar sus tareas pendientes (Backlog).
Debes implementar el sistema usando una LISTA ENLAZADA SIMPLE.

REQUERIMIENTOS:
1. (1.0) Clase Tarea: id (número), descripción (texto), prioridad (1-5, donde 5 es urgente).
2. (0.75) Método para agregar tarea garantizando que la lista esté ORDENADA por prioridad
   (de mayor a menor). Si tienen igual prioridad, la más reciente va primero.
3. (1.0) Método RECURSIVO para contar cuántas tareas tienen prioridad >= X.
4. (1.25) Método RECURSIVO para eliminar todas las tareas cuya descripción contenga cierta palabra clave.
5. (1.0) Método RECURSIVO para invertir el orden de la lista completa.
"""

import re

class Tarea:
    def __init__(self, id_tarea, descripcion, prioridad):
        self.id = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.siguiente = None

class Backlog:
    def __init__(self):
        self.cabeza = None

    # Punto 2: Agregar Ordenado (Iterativo o Recursivo, aquí Iterativo para variar)
    def agregar_tarea(self, id_tarea, descripcion, prioridad):
        nueva = Tarea(id_tarea, descripcion, prioridad)
        
        if self.cabeza is None or prioridad >= self.cabeza.prioridad:
            nueva.siguiente = self.cabeza
            self.cabeza = nueva
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.prioridad > prioridad:
            actual = actual.siguiente
        
        nueva.siguiente = actual.siguiente
        actual.siguiente = nueva

    # Punto 3: Contar tareas con prioridad >= X (Recursivo)
    def contar_urgentes(self, limite):
        return self._contar_urgentes_rec(self.cabeza, limite)

    def _contar_urgentes_rec(self, nodo, limite):
        if nodo is None:
            return 0
        conteo = 1 if nodo.prioridad >= limite else 0
        return conteo + self._contar_urgentes_rec(nodo.siguiente, limite)

    # Punto 4: Eliminar por palabra clave (Recursivo)
    def eliminar_por_palabra(self, palabra):
        self.cabeza = self._eliminar_por_palabra_rec(self.cabeza, palabra.lower())

    def _eliminar_por_palabra_rec(self, nodo, palabra):
        if nodo is None:
            return None
        
        # Primero procesar el resto de la lista
        nodo.siguiente = self._eliminar_por_palabra_rec(nodo.siguiente, palabra)
        
        # Si este nodo debe ser eliminado, retornar su siguiente
        if palabra in nodo.descripcion.lower():
            return nodo.siguiente
        
        return nodo

    # Punto 5: Invertir Lista (Recursivo)
    def invertir_lista(self):
        self.cabeza = self._invertir_rec(self.cabeza)

    def _invertir_rec(self, actual, anterior=None):
        if actual is None:
            return anterior
        siguiente = actual.siguiente
        actual.siguiente = anterior
        return self._invertir_rec(siguiente, actual)

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"[{actual.prioridad}] ID: {actual.id} - {actual.descripcion}")
            actual = actual.siguiente

# ═══════════════════════════════════════════════════════════════════════════════
#                    SIMULACRO PARCIAL 1 - MODELO B 
#                     SISTEMA UNDO/REDO (Pilas y Listas Dobles)
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
Un editor de texto minimalista necesita un sistema de Deshacer (Undo) y Rehacer (Redo).
Debes usar una LISTA DOBLEMENTE ENLAZADA para navegar entre estados.

REQUERIMIENTOS:
1. (1.0) Clase Estado: texto (string), timestamp (string hh:mm:ss).
2. (0.75) Clase Editor: Referencia al estado 'actual'.
3. (1.0) Método 'escribir': Agrega un nuevo estado después del actual y elimina los 
   estados que estaban adelante (si los había). Actualiza el puntero 'actual'.
4. (1.25) Método RECURSIVO 'buscar_texto': Retorna la cantidad de estados que contienen
   una palabra específica, buscando hacia ATRÁS desde el estado actual.
5. (1.0) Requisito Regex: Validar que el formato de timestamp sea correcto (00-23):(00-59):(00-59).
"""

import re

class Estado:
    def __init__(self, texto, timestamp):
        self.texto = texto
        self.timestamp = timestamp
        self.anterior = None
        self.siguiente = None

class Editor:
    def __init__(self):
        self.actual = None

    def validar_timestamp(self, ts):
        patron = r"^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
        return bool(re.match(patron, ts))

    def escribir(self, texto, ts):
        if not self.validar_timestamp(ts):
            print(f"Error: Timestamp {ts} inválido.")
            return

        nuevo = Estado(texto, ts)
        if self.actual is None:
            self.actual = nuevo
        else:
            # Eliminar lo que hay adelante (Redo log se pierde al escribir algo nuevo)
            nuevo.anterior = self.actual
            self.actual.siguiente = nuevo
            self.actual = nuevo

    def deshacer(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return True
        return False

    def rehacer(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return True
        return False

    def contar_ocurrencias_rec(self, palabra):
        return self._contar_atras(self.actual, palabra.lower())

    def _contar_atras(self, nodo, palabra):
        if nodo is None:
            return 0
        conteo = 1 if palabra in nodo.texto.lower() else 0
        return conteo + self._contar_atras(nodo.anterior, palabra)

# ═══════════════════════════════════════════════════════════════════════════════
#                    SIMULACRO PARCIAL 1 - MODELO C 
#                     GESTIÓN DE COLA DE IMPRESIÓN (Colas)
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
Una oficina tiene una impresora compartida. Los documentos tienen dueño y número de páginas.
Debes usar una COLA (Queue) implementada con Nodos.

REQUERIMIENTOS:
1. (1.0) Método 'encolar': Agrega documento al FINAL.
2. (1.0) Método RECURSIVO 'total_paginas': Suma las páginas de todos los documentos en cola.
3. (1.5) Método RECURSIVO 'filtrar_por_usuario': Retorna una NUEVA cola solo con documentos 
         de un usuario específico, sin vaciar la cola original.
4. (1.5) Método RECURSIVO 'desencolar_maximo': (DIFÍCIL) Busca el documento con más páginas,
         lo elimina de la cola y lo retorna. 
"""

class Documento:
    def __init__(self, usuario, paginas):
        self.usuario = usuario
        self.paginas = paginas
        self.siguiente = None

class ColaImpresion:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, usuario, paginas):
        nuevo = Documento(usuario, paginas)
        if self.ultimo:
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo
        if self.primero is None:
            self.primero = nuevo

    def total_paginas(self):
        return self._suma_rec(self.primero)

    def _suma_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.paginas + self._suma_rec(nodo.siguiente)

    def filtrar_por_usuario(self, user):
        nueva_cola = ColaImpresion()
        self._filtrar_rec(self.primero, user, nueva_cola)
        return nueva_cola

    def _filtrar_rec(self, nodo, user, nueva_cola):
        if nodo is None:
            return
        if nodo.usuario == user:
            nueva_cola.encolar(nodo.usuario, nodo.paginas)
        self._filtrar_rec(nodo.siguiente, user, nueva_cola)

    def mostrar(self):
        actual = self.primero
        while actual:
            print(f"[{actual.usuario} | {actual.paginas} pág]")
            actual = actual.siguiente

# ═══════════════════════════════════════════════════════════════════════════════
#                          EJECUCIÓN DE PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n--- PROBANDO MODELO A: BACKLOG ---")
    repo = Backlog()
    repo.agregar_tarea(1, "Fix bug en login", 5)
    repo.agregar_tarea(3, "Refactorizar BaseDatos", 4)
    repo.mostrar()

    print("\n--- PROBANDO MODELO B: EDITOR ---")
    edit = Editor()
    edit.escribir("Hola mundo", "12:30:00")
    edit.escribir("Hola curso", "12:35:00")
    edit.escribir("Otro texto", "12:40:00")
    print(f"Contar 'Hola' hacia atrás: {edit.contar_ocurrencias_rec('Hola')}")
    
    print("\n--- PROBANDO MODELO C: IMPRESORA ---")
    cola = ColaImpresion()
    cola.encolar("admin", 10)
    cola.encolar("juan", 5)
    cola.encolar("admin", 2)
    print(f"Total páginas: {cola.total_paginas()}")
    print("Documentos de 'admin':")
    cola.filtrar_por_usuario("admin").mostrar()

# ═══════════════════════════════════════════════════════════════════════════════
#                    SIMULACRO PARCIAL 1 - MODELO D 
#                     GESTIÓN DE REPUESTOS (Heaps y Sets)
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
Un taller mecánico necesita gestionar su inventario de repuestos y pedidos urgentes.

REQUERIMIENTOS:
1. (1.0) Clase Almacen: Almacena los repuestos usando un CONJUNTO (Set) para evitar duplicados.
2. (1.0) Método 'agregar_repuesto': Valida que el nombre del repuesto sea único antes de 
   agregarlo al conjunto.
3. (1.5) Cola de Pedidos: Los pedidos deben atenderse por PRIORIDAD (1-5) usando un HEAP.
4. (1.5) Método 'analizar_existencias': Recibe una lista de pedidos y retorna un conjunto
   con los repuestos que NO están disponibles en el almacén.
"""

import heapq

class Almacen:
    def __init__(self):
        self.repuestos = set()
        self.pedidos = [] # Heap de pedidos (Prioridad, Repuesto)

    def agregar_repuesto(self, nombre):
        self.repuestos.add(nombre.lower())

    def realizar_pedido(self, prioridad, repuesto):
        # 1 es máxima prioridad, 5 es mínima
        heapq.heappush(self.pedidos, (prioridad, repuesto.lower()))

    def atender_pedido(self):
        if self.pedidos:
            return heapq.heappop(self.pedidos)
        return None

    def repuestos_faltantes(self, lista_pedidos):
        # lista_pedidos es una lista de strings
        pedidos_set = {p.lower() for p in lista_pedidos}
        return pedidos_set - self.repuestos # Diferencia de conjuntos

# ═══════════════════════════════════════════════════════════════════════════════
#                          EJECUCIÓN DE PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n--- PROBANDO MODELO D: TALLER ---")
    taller = Almacen()
    taller.agregar_repuesto("Bujía")
    taller.agregar_repuesto("Aceite")
    taller.agregar_repuesto("Filtro")
    
    faltantes = taller.repuestos_faltantes(["Bujía", "Llantas", "Espejo"])
    print(f"Repuestos faltantes: {faltantes}")
    
    taller.realizar_pedido(2, "Aceite")
    taller.realizar_pedido(1, "Bujía")
    prio, item = taller.atender_pedido()
    print(f"Atendiendo pedido urgente: {item} (Prioridad {prio})")
