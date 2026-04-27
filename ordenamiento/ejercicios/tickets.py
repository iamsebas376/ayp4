class Ticket:
    def __init__(self, id_ticket, prioridad, tiempo):
        self.id_ticket = id_ticket
        self.prioridad = prioridad
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"ID: {self.id_ticket}, Prioridad: {self.prioridad}, Tiempo: {self.tiempo}"

class ColaTickets:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, id_ticket, prioridad, tiempo):
        nuevo_ticket = Ticket(id_ticket, prioridad, tiempo)
        if self.cabeza is None:
            self.cabeza = nuevo_ticket
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_ticket

    def mostrar(self):
        actual = self.cabeza
        pos = 1
        while actual:
            print(f"Posición {pos}: {actual}")
            actual = actual.siguiente
            pos += 1

    def longitud(self):
        actual = self.cabeza
        longitud = 0
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud

    def ordenar_burbuja(self):
        longitud = self.longitud()
        intercambios = 0
        for i in range(longitud):
            actual = self.cabeza
            for j in range(0, longitud - i - 1):
                if actual.prioridad > actual.siguiente.prioridad:
                    # Intercambiar todos los atributos de los tickets
                    actual.id_ticket, actual.siguiente.id_ticket = actual.siguiente.id_ticket, actual.id_ticket
                    actual.prioridad, actual.siguiente.prioridad = actual.siguiente.prioridad, actual.prioridad
                    actual.tiempo, actual.siguiente.tiempo = actual.siguiente.tiempo, actual.tiempo
                    intercambios += 1
                actual = actual.siguiente
        return self.mostrar(), intercambios


if __name__ == "__main__":
    cola_tickets = ColaTickets()
    cola_tickets.agregar(1, 3, 10)
    cola_tickets.agregar(2, 1, 5)
    cola_tickets.agregar(3, 2, 15)
    cola_tickets.agregar(4, 3, 7)
    cola_tickets.agregar(5, 1, 3)

    print("Cola de tickets original:")
    cola_tickets.mostrar()
    print("\nCola de tickets ordenada:")
    cola_tickets.ordenar_burbuja()
