# 📚 GUÍA MAESTRA PARA EL PARCIAL (NOTAS COMPACTAS)

Esta guía resume las plantillas y patrones clave que necesitas para resolver los ejercicios del parcial.

## 1. Expresiones Regulares (Regex)
Importante: Siempre `import re`.

*   **re.match(patron, string):** Valida DESDE EL INICIO del string.
*   **re.findall(patron, string):** Retorna una LISTA de todas las ocurrencias.

**Patrones Comunes:**
-   `^\d{3}$`: Exactamente 3 números.
-   `^[A-Z]{2,4}$`: Mayúsculas, entre 2 y 4 caracteres.
-   `[a-zA-Z]+`: Cualquier secuencia de letras.
-   `\w+`: Caracteres alfanuméricos (letras, números, guión bajo).
-   `r"#\w+"`: Encuentra hashtags (#hola).
-   `r"@\w+"`: Encuentra menciones (@sebas).

---

## 2. Estructuras de Datos con Nodos
Todas se basan en la clase base:
```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        # self.anterior = None (Si es doble)
```

**Operaciones Clave:**
-   **Apilar (Stack/Pila):** Agregar al inicio (`nuevo.sig = self.tope; self.tope = nuevo`).
-   **Encolar (Queue/Cola):** Agregar al final (`self.ultimo.sig = nuevo; self.ultimo = nuevo`).
-   **Circular:** Siempre `self.ultimo.siguiente = self.primero`.
-   **Invertir Recursivo:** Ver `simulacro_1`.

---

## 3. Recursividad
Estructura obligatoria:
1.  **Caso Base:** Detiene la ejecución (ej: `if nodo is None: return 0`).
2.  **Llamada Recursiva:** Procesa el siguiente elemento (`return nodo.valor + suma_rec(nodo.siguiente)`).

**Tip: Recursión en Circular:**
Pasa un parámetro `inicio` para saber cuándo has dado la vuelta completa.
```python
def recorrer(self, actual, inicio=None):
    if not inicio: inicio = actual
    if actual.siguiente == inicio: return # Caso base
    recorrer(actual.siguiente, inicio)
```

---

## 4. Conjuntos (Sets)
Eficaces para unicidad y comparación. Suelen usarse para categorías, ciudades o permisos.

*   `s1 | s2`: **Unión** (Todo lo de ambos).
*   `s1 & s2`: **Intersección** (Lo que tienen en común).
*   `s1 - s2`: **Diferencia** (Lo que está en s1 pero no en s2).
*   `s.add(x)`: Agrega solo si no existe.

---

## 5. Memorización (Caché)
Usa un diccionario (`self.cache = {}`) para guardar resultados ya calculados y evitar colapsar la recursividad.

**Esquema:**
```python
def funcion_memo(self, n):
    if n in self.cache: return self.cache[n] # 1. Chequear caché
    
    # ... proceso normal ...
    
    self.cache[n] = resultado # 2. Guardar en caché antes de retornar
    return resultado
```

---

## 🗂️ Archivos de Práctica Generados:
-   `practica_1_logistica.py`: Stacks + Regex + Memo.
-   `practica_2_red_social.py`: Listas Dobles + Sets Intersection.
-   `practica_3_inventario_circular.py`: Circular + Set Difference.
-   `practica_4_calculadora_finanzas.py`: Recursión Compleja + Memoización.
