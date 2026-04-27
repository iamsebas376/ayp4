# PRACTICA 6: GESTIÓN DE RESERVAS DE HOTEL
# TEMAS: REGEX (Fechas DD/MM/YYYY) + SETS (Diferencia de Habitaciones) + RECURSIVIDAD SIMPLE

import re

class Hotel:
    def __init__(self, n_pisos, n_habs):
        self.habitaciones_totales = {f"{p}{h:02d}" for p in range(1, n_pisos+1) for h in range(1, n_habs+1)}
        self.reservas = {} # Fecha -> Habitaciones Ocupadas (Set)

    def validar_fecha(self, fecha):
        # Regex para DD/MM/YYYY
        patron = r"^([0-2][0-9]|3[01])/(0[1-9]|1[0-2])/(20\d{2})$"
        return bool(re.match(patron, fecha))

    def reservar(self, fecha, hab_num):
        if not self.validar_fecha(fecha):
            print(f"Error: Fecha {fecha} inválida.")
            return

        if hab_num not in self.habitaciones_totales:
            print(f"Error: Habitación {hab_num} no existe.")
            return

        if fecha not in self.reservas:
            self.reservas[fecha] = set()
        
        self.reservas[fecha].add(hab_num)
        print(f"Habitación {hab_num} reservada para {fecha}.")

    def disponibles_en_fecha(self, fecha):
        if fecha not in self.reservas:
            return self.habitaciones_totales
        
        # DIFERENCIA: Totales - Ocupadas
        return self.habitaciones_totales - self.reservas[fecha]

    def listar_disponibles_rec(self, lista_habs):
        """Muestra las habs disponibles recursivamente."""
        if not lista_habs:
            return
        
        actual = lista_habs[0]
        print(f" - Disponible: {actual}")
        self.listar_disponibles_rec(lista_habs[1:])

if __name__ == "__main__":
    h = Hotel(3, 5) # 3 pisos, 5 habs por piso (315, 314, etc.)
    
    h.reservar("15/10/2026", "101")
    h.reservar("15/10/2026", "205")
    h.reservar("fecha-loca", "303") # Fallará por Regex
    
    print("\n--- Habitaciones Libres para 15/10 ---")
    libres = h.disponibles_en_fecha("15/10/2026")
    h.listar_disponibles_rec(sorted(list(libres)))
