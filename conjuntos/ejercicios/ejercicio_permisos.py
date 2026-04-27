"""
EJERCICIO: Sistema de Permisos de Usuario
Contexto: Un sistema de archivos tiene usuarios, grupos y permisos.
Los permisos se manejan como conjuntos para facilitar las operaciones.
"""

# Permisos disponibles
PERMISOS_VALIDOS = {"lectura", "escritura", "ejecucion", "eliminacion", "administracion"}

# Roles predefinidos
rol_invitado = {"lectura"}
rol_editor = {"lectura", "escritura"}
rol_programador = {"lectura", "escritura", "ejecucion"}
rol_admin = PERMISOS_VALIDOS.copy()

def analizar_permisos(nombre_usuario, permisos_actuales, permisos_requeridos):
    print(f"\n--- Analizando usuario: {nombre_usuario} ---")
    print(f"Permisos actuales: {permisos_actuales}")
    print(f"Permisos requeridos para la acción: {permisos_requeridos}")
    
    # 1. ¿Tiene todos los permisos necesarios? (Subconjunto)
    tiene_acceso = permisos_requeridos.issubset(permisos_actuales)
    
    # 2. ¿Qué permisos le faltan? (Diferencia)
    faltantes = permisos_requeridos - permisos_actuales
    
    # 3. Permisos extra que tiene y no son necesarios (Diferencia)
    extras = permisos_actuales - permisos_requeridos
    
    # 4. ¿Hay algún permiso inválido otorgado? (Diferencia con los válidos)
    invalidos = permisos_actuales - PERMISOS_VALIDOS
    
    if tiene_acceso:
        print("ESTADO: ACCESO CONCEDIDO")
    else:
        print(f"ESTADO: ACCESO DENEGADO. Faltan: {faltantes}")
        
    if invalidos:
        print(f"ALERTA: Se detectaron permisos no válidos o desconocidos: {invalidos}")

# Simulaciones
permisos_juan = {"lectura", "escritura", "borrado_temporal"} # 'borrado_temporal' no es válido
accion_modificar_sistema = {"lectura", "escritura", "ejecucion"}

analizar_permisos("Juan", permisos_juan, accion_modificar_sistema)
analizar_permisos("Admin", rol_admin, accion_modificar_sistema)
