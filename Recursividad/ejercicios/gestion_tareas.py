class Tarea:
    def __init__(self, nombre, tiempo_estimado, completada=False):
        self.nombre = nombre
        self.tiempo_estimado = tiempo_estimado
        self.completada = completada
        self.subtareas = []

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    # 1. EJERCICIO: Calcular el tiempo total estimado de una tarea y todas sus subtareas
    def tiempo_total(self):
        total = self.tiempo_estimado
        for sub in self.subtareas:
            total += sub.tiempo_total()
        return total

    # 2. EJERCICIO: Contar cuántas tareas en total (incluyendo subtareas) están completadas
    def contar_completadas(self):
        count = 1 if self.completada else 0
        for sub in self.subtareas:
            count += sub.contar_completadas()
        return count

    # 3. EJERCICIO: Calcular el porcentaje de progreso real basado en el tiempo
    def calcular_progreso_tiempo(self):
        tiempo_listo = self._obtener_tiempo_completado()
        total = self.tiempo_total()
        return (tiempo_listo / total) * 100 if total > 0 else 0

    def _obtener_tiempo_completado(self):
        tiempo = self.tiempo_estimado if self.completada else 0
        for sub in self.subtareas:
            tiempo += sub._obtener_tiempo_completado()
        return tiempo

proyecto = Tarea("Desarrollo App Movil", 100)

front = Tarea("Frontend", 40, True)
back = Tarea("Backend", 60)

proyecto.agregar_subtarea(front)
proyecto.agregar_subtarea(back)

db = Tarea("Base de Datos", 20, True)
api = Tarea("API REST", 30)
auth = Tarea("Autenticación", 10, True)

back.agregar_subtarea(db)
back.agregar_subtarea(api)
back.agregar_subtarea(auth)

ui = Tarea("Diseño UI", 15, True)
red = Tarea("Integración Red", 25, True)

front.agregar_subtarea(ui)
front.agregar_subtarea(red)

print(f"Proyecto: {proyecto.nombre}")
print(f"Tiempo total estimado: {proyecto.tiempo_total()} horas")
print(f"Número de tareas completadas: {proyecto.contar_completadas()}")
print(f"Progreso del proyecto: {proyecto.calcular_progreso_tiempo()}%")
