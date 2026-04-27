estudiantes_algoritmos = {
    "Juan",
    "Maria",
    "Pedro",
    "Ana",
    "Carlos",
    "Laura",
    "Miguel",
    "Elena"
}

estudiantes_base_datos = {
    "Juan",
    "Maria",
    "Pedro",
    "Ana",
    "Luis",
    "Sofia",
}

estudiantes_redes = {
    "Juan",
    "Maria",
    "Pedro",
    "Carlos",
    "Laura",
    "Miguel",
    "Elena"
}

# Estudiantes que estudian todas las materias
estudiantes_todas = estudiantes_algoritmos.intersection(estudiantes_base_datos, estudiantes_redes)
print("\nEstudiantes que estudian todas las materias: ", estudiantes_todas)

# Estudiantes que solo estudian una materia
estudiantes_solo_una = estudiantes_algoritmos.difference(estudiantes_base_datos, estudiantes_redes).union(estudiantes_base_datos.difference(estudiantes_algoritmos, estudiantes_redes)).union(estudiantes_redes.difference(estudiantes_algoritmos, estudiantes_base_datos))
print("\nEstudiantes que solo estudian una materia: ", estudiantes_solo_una)

# Materias en que está cada estudiante con un diccionario y condicionales

reporte = {}

todos_los_estudiantes = estudiantes_algoritmos | estudiantes_base_datos | estudiantes_redes

for estudiante in todos_los_estudiantes:
    materias = []
    if estudiante in estudiantes_algoritmos: 
        materias.append("Algoritmos")
    if estudiante in estudiantes_base_datos:
        materias.append("Base de Datos")
    if estudiante in estudiantes_redes:
        materias.append("Redes")
    reporte[estudiante] = materias

print("\nReporte de estudiantes:", reporte)



