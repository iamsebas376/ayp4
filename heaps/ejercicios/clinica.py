# Ejercicio para ingresar pacientes a una clínica, cada paciente tiene un nombre y una prioridad (1, 2 o 3).
# Se debe ingresar el paciente con mayor prioridad primero, y en caso de empate, el paciente que ingresó primero.
# Utilizar un heap para gestionar la cola de pacientes.
# Se usan tuplas (prioridad, nombre) para almacenar los pacientes en el heap.
# Menú para agregar pacientes, atender pacientes y mostrar la lista de espera.

import heapq

class Clinica:
    def __init__(self):
        self.pacientes = []
        self.orden_llegada = 0

    def agregar_paciente(self, nombre, prioridad):
        heapq.heappush(self.pacientes, (prioridad, self.orden_llegada, nombre))
        print(f"Paciente '{nombre}' con orden de llegada {self.orden_llegada} con prioridad {prioridad} agregado a la lista de espera.")
        self.orden_llegada += 1

    def atender_paciente(self):
        if not self.pacientes:
            print("No hay pacientes en la lista de espera.")
            return
        prioridad, self.orden, nombre = heapq.heappop(self.pacientes)
        print(f"Atendiendo al paciente '{nombre}' con prioridad {prioridad}.")

    def mostrar_lista_espera(self):
        if not self.pacientes:
            print("No hay pacientes en la lista de espera.")
            return
        print("Lista de espera:")
        for prioridad, orden, nombre in sorted(self.pacientes):
            print(f"Paciente: {nombre}, Orden de llegada: {orden}, Prioridad: {prioridad}")


clinica = Clinica()

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar paciente")
        print("2. Atender paciente")
        print("3. Mostrar lista de espera")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            prioridad = int(input("Ingrese la prioridad (1, 2 o 3): "))
            clinica.agregar_paciente(nombre, prioridad)
        elif opcion == "2":
            clinica.atender_paciente()
        elif opcion == "3":
            clinica.mostrar_lista_espera()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    clinica.agregar_paciente("Juan", 2)
    clinica.agregar_paciente("Ana", 1)
    clinica.agregar_paciente("Luis", 3)
    menu()