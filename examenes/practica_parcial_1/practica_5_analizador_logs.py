# PRACTICA 5: ANALIZADOR DE LOGS DE SERVIDOR
# TEMAS: REGEX (IPs y Errores) + HEAPS (Prioridad de atención) + SETS (IPs Maliciosas)

import re
import heapq

class Servidor:
    def __init__(self):
        self.cola_emergencias = [] # Heap
        self.ips_bloqueadas = {"192.168.1.50", "200.5.10.1"} # Sets

    def procesar_log(self, linea):
        # Regex para extraer IP (4 grupos de números)
        ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        # Regex para extraer código de error (Ej: ERROR 500)
        error_pattern = r"ERROR (\d{3})"
        
        ip = re.search(ip_pattern, linea)
        error = re.search(error_pattern, linea)
        
        if ip and error:
            ip_val = ip.group(1)
            cod_err = int(error.group(1))
            
            # Si el error es crítico (500s), va al HEAP con alta prioridad (menor número primero)
            # Prioridad = 1 para errores 500, Prioridad = 5 para errores 400
            prioridad = 1 if cod_err >= 500 else 5
            
            if ip_val in self.ips_bloqueadas:
                print(f"ALERTA: Intento de acceso de IP Bloqueada: {ip_val}")
            else:
                # Metemos al heap: (prioridad, mensaje)
                heapq.heappush(self.cola_emergencias, (prioridad, f"Error {cod_err} de IP {ip_val}"))

    def atender_siguiente(self):
        if self.cola_emergencias:
            prioridad, msj = heapq.heappop(self.cola_emergencias)
            print(f"Atendiendo (Prio {prioridad}): {msj}")

if __name__ == "__main__":
    srv = Servidor()
    srv.procesar_log("10.0.0.1 - [10/Oct] - ERROR 404")
    srv.procesar_log("192.168.1.50 - [10/Oct] - ERROR 500") # IP Bloqueada
    srv.procesar_log("172.16.2.3 - [10/Oct] - ERROR 503") # Crítico
    
    print("\n--- Despachando Errores del Heap ---")
    srv.atender_siguiente()
    srv.atender_siguiente()
