"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n)
# Porque: Realiza un ciclo for que recorre todos los elementos una sola vez.


def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n^2)
# Porque: Tiene dos ciclos anidados que recorren la lista de tamaño n.


def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(log n)
# Porque: En cada llamada recursiva, el valor de n se divide a la mitad.


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque: Aunque añadir a un set es constante O(1), la función lo hace n veces dentro de un ciclo.


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n^2)
# Porque: El for corre n veces, y la operación x in lista también es constante, al estar anidados se multiplican.
# PISTA: ¿cuánto cuesta `x in lista`?


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(n log n)
# Porque: El for es linea, y el while es logarítmico, al estar aninados se multiplican.


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n log n)
# Porque: La lista se divide en cada paso 0(log n), pero las operaciones de slicing son lineales, por lo tanto se multiplica la complejidad.
# PISTA: ¿cuánto cuesta lista[:medio]?


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(√n)
# Porque: El ciclo while se detiene cuando i*i supera n, lo que significa que i llega hasta la raíz cuadrada de n.


"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(√n)
4. O(n)
5. O(n log n)
6. O(n²)
7. O(n³)
8. O(2^n)
9. O(n!)
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. Falso. O(2n) es más lento que O(n)
   Justificación: Las constantes se ignoran.

2. Verdadero. Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación: A medida que n crece, n^2 siempre superará a n \log n.

3. Falso. Si un algoritmo tiene un for de n y dentro un for de 5,
       su complejidad es O(n²)
   Justificación: Un ciclo interno de valor constante no afecta la linealidad.

4. Falso. `x in set` tiene la misma complejidad que `x in list`
   Justificación: La búsqueda en un set es constante, y en un list es lineal.

5. Faslo. Un algoritmo recursivo que se llama a sí mismo 2 veces
       siempre es O(2^n)
   Justificación: Depende de como se reduzca el problema.

6. Falso. O(n) + O(n²) = O(n³)
   Justificación: En la suma de complejidad, se conserva únicamente el término de orden mayor.

7. Verdadero. La complejidad espacial de un algoritmo in-place es O(1)
   Justificación: Un algortimo in-place solo utiliza una cantida pequeña y constante de memoria extra, independiente a la entrada.

8. Verdadero. Memoización mejora la complejidad temporal pero empeora la espacial
   Justificación: La meoización ahorra tiempo reutilizando cálculos, pero requiere almacenar esos resultados en memoria.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)         │
│ Agregar al final (.append)   │ O(1)         │ O(1) (.add)  │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1)         │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘
"""


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: Timsort (un híbrido de Merge Sort e Insertion Sort).

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: O(n) - cuando la lista ya está casi ordenada.
   Peor: O(n log n)
   Promedio: O(n log n)

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta: Timsort es estable (mantiene el orden relativo de elementos iguales) y es extremadamente eficiente con datos que contienen "runs" (secuencias ya ordenadas), lo cual es común en aplicaciones reales. Quick Sort, aunque rápido, no es estable y tiene un peor caso de O(n²) sin pivotes aleatorios.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    COMPLEJIDAD: O(n) - recorre la lista una vez y las operaciones de set son O(1).
    """
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)
    return resultado


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    COMPLEJIDAD: O(n) - un recorrido para contar y otro (sobre las llaves) para encontrar el máximo.
    """
    if not lista: return None, 0
    conteo = {}
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
    
    max_elem = None
    max_count = 0
    for x, count in conteo.items():
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    COMPLEJIDAD: O(n) - recorre la lista una vez realizando búsquedas constantes en el set.
    """
    pares = []
    vistos = set()
    for x in lista:
        complemento = k - x
        if complemento in vistos:
            # Para coincidir con el comportamiento de pares_suma_lento que encuentra pares por índices
            # y puede repetir elementos si aparecen varias veces:
            # El lento devuelve (lista[i], lista[j]), vamos a imitarlo.
            # Nota: el lento devuelve pares basados en el orden de los índices.
            # Aquí añadimos (complemento, x) para mantener una consistencia lógica.
            pares.append((complemento, x))
        vistos.add(x)
    return pares


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    COMPLEJIDAD: O(n) - donde n es la longitud de las palabras. Se recorren una vez para contar.
    """
    if len(palabra1) != len(palabra2):
        return False
    
    conteo = {}
    for letra in palabra1:
        conteo[letra] = conteo.get(letra, 0) + 1
    
    for letra in palabra2:
        if letra not in conteo or conteo[letra] == 0:
            return False
        conteo[letra] -= 1
    
    return True


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(n³)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    COMPLEJIDAD: O(n) - un solo ciclo que recorre la lista.
    """
    if not lista: return 0
    max_suma = lista[0]
    suma_actual = lista[0]
    
    for i in range(1, len(lista)):
        suma_actual = max(lista[i], suma_actual + lista[i])
        max_suma = max(max_suma, suma_actual)
        
    return max_suma


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: Recorrer toda la lista de palabras y verificar si cada una empieza con el prefijo usando .startswith().
  Complejidad: O(N * M) donde N es el número de palabras y M la longitud del prefijo.
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(N * M)
    """
    resultado = []
    for p in palabras:
        if p.startswith(prefijo):
            resultado.append(p)
            if len(resultado) == 5:
                break
    return resultado


"""
SOLUCIÓN 2 (optimizada):
  Descripción: Usar búsqueda binaria para encontrar el primer elemento que empiece con el prefijo y recolectar los siguientes 5 si coinciden.
  Complejidad: O(M * log N) para la búsqueda binaria.
  ¿Qué estructura de datos usarías? Una lista ordenada o un Trié (árbol de prefijos) para máxima eficiencia.
  Código:
"""

import bisect

def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(M * log N)
    """
    idx = bisect.bisect_left(palabras_ordenadas, prefijo)
    resultado = []
    for i in range(idx, min(idx + 5, len(palabras_ordenadas))):
        if palabras_ordenadas[i].startswith(prefijo):
            resultado.append(palabras_ordenadas[i])
        else:
            break
    return resultado


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(A) donde A es el número de amigos (promedio 200).
   - Con set de amigos: O(1) promedio.
   - ¿Cuál elegirías? Set de amigos.

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(A1 * A2)
   - Con sets: O(min(A1, A2)) usando intersección de sets.
   - ¿Cuál elegirías? Sets.

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: Obtener los sets de amigos de todos mis amigos, unirlos en un set global de "candidatos", y restar mi propio set de amigos y a mí mismo.
   - Complejidad estimada: O(A * A') donde A es mi número de amigos y A' el promedio de sus amigos.
   - ¿Es viable para 10M de usuarios? Sí, porque la operación es local al grafo del usuario (200 * 200 = 40,000 operaciones), no depende de los 10M totales directamente.

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
   - Con lista: 10M * 200 * 8 bytes (aprox 16 GB)
   - Con set: Un poco más debido al overhead de la tabla hash (aprox 24-30 GB)
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
Analizar la complejidad antes de implementar es crucial porque permite prever el comportamiento del sistema bajo carga real sin desperdiciar recursos. Un algoritmo ineficiente puede funcionar bien con 10 datos, pero fallar catastróficamente con 1 millón. Por ejemplo, en una plataforma de e-commerce, usar una búsqueda lineal O(n) para filtrar productos entre millones de entradas en lugar de una búsqueda indexada O(log n) o O(1) causaría tiempos de respuesta de varios segundos. Esto resultaría en una mala experiencia de usuario, pérdida de ventas y un aumento masivo en los costos de infraestructura de servidores al procesar peticiones innecesariamente largas. La eficiencia algorítmica es a menudo la diferencia entre un producto escalable y uno que colapsa.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)") 
