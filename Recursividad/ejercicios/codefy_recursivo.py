class Cancion:
    def __init__(self, nombre, artista, genero, album, anio, duracion):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.album = album
        self.anio = anio
        self.duracion = duracion

    def __str__(self):
        return f"{self.nombre} - {self.artista} ({self.anio}) [{self.genero}] | {self.album} | {self.duracion}"

class Node:
    def __init__(self, cancion):
        self.dato = cancion
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None
        self.cola = None
        self.actual = None
        self._cantidad = 0

    def repetir_lista(self):
        self.actual = self.cabeza
        return self.actual.dato if self.actual else None

    def _duracion_rec(self, nodo):
        if not nodo:
            return 0
        try:
            minutos, segundos = map(int, nodo.dato.duracion.split(':'))
            total = minutos * 60 + segundos
        except ValueError:
            total = 0
        return total + self._duracion_rec(nodo.siguiente)

    def duracion_total(self):
        total_segundos = self._duracion_rec(self.cabeza)
        minutos, segundos = divmod(total_segundos, 60)
        return f"{minutos}:{str(segundos).zfill(2)}"

    def _cantidad_rec(self, nodo):
        if not nodo:
            return 0
        return 1 + self._cantidad_rec(nodo.siguiente)

    def cantidad(self):
        return self._cantidad_rec(self.cabeza)

    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.dato
        return None

    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual.dato
        return None

    def ir_primera(self):
        if self.cabeza:
            self.actual = self.cabeza
            return self.actual.dato
        return None

    def ir_ultima(self):
        if self.cola:
            self.actual = self.cola
            return self.actual.dato
        return None

    def _reproducir_por_rec(self, nodo, criterio, valor):
        if not nodo:
            return None
        if getattr(nodo.dato, criterio, '').__str__().lower() == str(valor).lower():
            self.actual = nodo
            return nodo.dato
        return self._reproducir_por_rec(nodo.siguiente, criterio, valor)

    def reproducir_por(self, criterio, valor):
        return self._reproducir_por_rec(self.cabeza, criterio, valor)

    def obtener_actual(self):
        if self.actual:
            return self.actual.dato
        return None
    
    def esta_vacia(self):
        return self.cabeza is None

    # Insertar final (versión usando cola es O(1), pero recursiva por ejercicio)
    # Si usamos recursión pura sin cola:
    def _insertar_final_rec(self, nodo, nuevo):
        if nodo.siguiente is None:
            nodo.siguiente = nuevo
            nuevo.anterior = nodo
            self.cola = nuevo # Actualizamos cola
            return
        self._insertar_final_rec(nodo.siguiente, nuevo)

    def insertar_final(self, cancion):
        nuevo = Node(cancion)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            # Opción 1: Usar recursión para llegar al final
            self._insertar_final_rec(self.cabeza, nuevo)
            # Opción 2: Usar self.cola directo (más eficiente, pero menos "recursivo")
            # Para fines educativos:
            pass
        self._cantidad += 1

    def insertar_inicio(self, cancion):
        nuevo = Node(cancion)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self._cantidad += 1

    def _insertar_pos_rec(self, nodo, cancion, indice_actual, indice_objetivo):
        if indice_actual == indice_objetivo:
            nuevo = Node(cancion)
            anterior = nodo.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = nodo
            nodo.anterior = nuevo
            return
        if nodo.siguiente:
            self._insertar_pos_rec(nodo.siguiente, cancion, indice_actual + 1, indice_objetivo)

    def insertar_en_posicion(self, cancion, posicion):
        if posicion <= 0:
            self.insertar_inicio(cancion)
        elif posicion >= self.cantidad(): # Usamos cantidad recursiva
            self.insertar_final(cancion)
        else:
            # Buscar recursivamente la posición
            # Empezamos en índice 0 (cabeza)
            # Queremos insertar UNTES del nodo en 'posicion'
            self._insertar_pos_rec(self.cabeza, cancion, 0, posicion)
            self._cantidad += 1

    def _eliminar_rec(self, nodo, nombre):
        if not nodo:
            return False
        if nodo.dato.nombre.lower() == nombre.lower():
            # Eliminar nodo
            if nodo.anterior:
                nodo.anterior.siguiente = nodo.siguiente
            else:
                self.cabeza = nodo.siguiente
            
            if nodo.siguiente:
                nodo.siguiente.anterior = nodo.anterior
            else:
                self.cola = nodo.anterior
            return True
        return self._eliminar_rec(nodo.siguiente, nombre)

    def eliminar_por_nombre(self, nombre):
        exito = self._eliminar_rec(self.cabeza, nombre)
        if exito:
            self._cantidad -= 1
        return exito

    def _buscar_rec(self, nodo, nombre):
        if not nodo:
            return None
        if nodo.dato.nombre.lower() == nombre.lower():
            return nodo.dato
        return self._buscar_rec(nodo.siguiente, nombre)

    def buscar(self, nombre):
        return self._buscar_rec(self.cabeza, nombre)

    def _str_rec(self, nodo):
        if not nodo:
            return []
        return [str(nodo.dato)] + self._str_rec(nodo.siguiente)

    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"
        elementos = self._str_rec(self.cabeza)
        return "\n".join(elementos)

class Reproductor:
    def __init__(self, nombre_playlist):
        self.lista = ListaDoble(nombre_playlist)
        self.cancion_actual = None
        self.repetir_lista = False

    def siguiente(self):
        self.cancion_actual = self.lista.siguiente()
        return self.cancion_actual

    def anterior(self):
        self.cancion_actual = self.lista.anterior()
        return self.cancion_actual

    def ir_primera(self):
        self.cancion_actual = self.lista.ir_primera()
        return self.cancion_actual

    def ir_ultima(self):
        self.cancion_actual = self.lista.ir_ultima()
        return self.cancion_actual

    def reproducir_por(self, criterio, valor):
        self.cancion_actual = self.lista.reproducir_por(criterio, valor)
        return self.cancion_actual

    def repetir_lista(self):
        self.cancion_actual = self.lista.repetir_lista()
        return self.cancion_actual

    def obtener_actual(self):
        self.cancion_actual = self.lista.obtener_actual()
        return self.cancion_actual

class InterfazConsola:
    def __init__(self, reproductor):
        self.reproductor = reproductor

    def mostrar_menu(self):
        print("\n" + "="*45)
        print("--- CODEFY MP3 (RECURSIVO) ---")
        print("="*45)
        print("1. Mostrar canciones")
        print("2. Agregar canción")
        print("3. Eliminar canción")
        print("4. Buscar canción")
        print("5. Menú de Reproducción")
        print("6. Estadísticas de la lista")
        print("7. Editar canción")
        print("0. Salir")
        print("="*45)

    def pedir_datos_cancion(self):
        print("Ingrese los datos de la canción:")
        while True:
            nombre = input("- Nombre: ").strip()
            artista = input("- Artista: ").strip()
            genero = input("- Género: ").strip()
            album = input("- Álbum: ").strip()
            anio = input("- Año: ").strip()
            duracion = input("- Duración (mm:ss): ").strip()

            if not (nombre and artista and genero and album and anio and duracion):
                print("Todos los campos son obligatorios.")
                continue
            if not anio.isdigit():
                print("El año debe ser un número entero.")
                continue
            try:
                minutos, segundos = duracion.split(":")
                minutos = int(minutos)
                segundos = int(segundos)
                if minutos < 0 or segundos < 0 or segundos >= 60:
                    raise ValueError
            except Exception:
                print("Duración inválida. Usa el formato mm:ss.")
                continue
            return Cancion(nombre, artista, genero, album, int(anio), duracion)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("> Selecciona una opción: ")

            if opcion == "1":
                print("\n" + "="*45)
                print("--- LISTA DE CANCIONES ---")
                print("="*45)
                print(self.reproductor.lista)

            elif opcion == "2":
                print("\n" + "="*45)
                print("--- AGREGAR CANCIÓN ---")
                print("="*45)
                cancion = self.pedir_datos_cancion()
                print("\n¿Dónde deseas insertar la canción?")
                print("1. Al inicio")
                print("2. Al final (Predeterminado)")
                print("3. Posición específica")
                subop = input("> Elige una opción: ")
                
                if subop == "1":
                    self.reproductor.lista.insertar_inicio(cancion)
                elif subop == "3":
                    try:
                        pos = int(input(f"Posición (0 a {self.reproductor.lista.cantidad()}): "))
                    except ValueError:
                        pos = self.reproductor.lista.cantidad()
                    self.reproductor.lista.insertar_en_posicion(cancion, pos)
                else:
                    self.reproductor.lista.insertar_final(cancion)
                print("Canción agregada con éxito.")
            elif opcion == "3":
                print("\n" + "="*45)
                print("--- ELIMINAR CANCIÓN ---")
                print("="*45)
                nombre = input("Nombre de la canción a eliminar: ")
                if self.reproductor.lista.eliminar_por_nombre(nombre):
                     print(f"La canción '{nombre}' ha sido eliminada.")
                else:
                     print(f"No se encontró la canción '{nombre}'.")

            elif opcion == "4":
                print("\n" + "="*45)
                print("--- BUSCAR CANCIÓN ---")
                print("="*45)
                nombre = input("Nombre de la canción: ")
                cancion = self.reproductor.lista.buscar(nombre)
                if cancion:
                    print("Encontrada:", cancion)
                else:
                    print("No se encontró la canción.")

            elif opcion == "5":
                self.menu_navegacion()

            elif opcion == "6":
                print("\n" + "="*45)
                print("--- ESTADÍSTICAS ---")
                print("="*45)
                print("="*45)
                print(f"Cantidad de canciones: {self.reproductor.lista.cantidad()}")
                print(f"Duración total: {self.reproductor.lista.duracion_total()}")

            elif opcion == "7":
                print("\n" + "="*45)
                print("--- EDITAR CANCIÓN ---")
                print("="*45)
                nombre = input("Nombre de la canción a editar: ")
                nodo = self.reproductor.lista.cabeza
                encontrado = False
                while nodo:
                    if nodo.dato.nombre.lower() == nombre.lower():
                        encontrado = True
                        print("\nEditando:", nodo.dato)
                        print("(Deja en blanco para mantener el valor actual)")
                        
                        nuevo_nombre = input(f"- Nuevo nombre [{nodo.dato.nombre}]: ").strip()
                        if nuevo_nombre: nodo.dato.nombre = nuevo_nombre
                        
                        nuevo_artista = input(f"- Nuevo artista [{nodo.dato.artista}]: ").strip()
                        if nuevo_artista: nodo.dato.artista = nuevo_artista
                        
                        nuevo_genero = input(f"- Nuevo género [{nodo.dato.genero}]: ").strip()
                        if nuevo_genero: nodo.dato.genero = nuevo_genero
                        
                        nuevo_album = input(f"- Nuevo álbum [{nodo.dato.album}]: ").strip()
                        if nuevo_album: nodo.dato.album = nuevo_album
                        
                        nuevo_anio = input(f"- Nuevo año [{nodo.dato.anio}]: ").strip()
                        if nuevo_anio.isdigit(): nodo.dato.anio = int(nuevo_anio)
                        
                        nuevo_duracion = input(f"- Nueva duración [{nodo.dato.duracion}]: ").strip()
                        if nuevo_duracion:
                            try:
                                m, s = nuevo_duracion.split(":")
                                if int(m) >= 0 and 0 <= int(s) < 60:
                                    nodo.dato.duracion = nuevo_duracion
                                else: raise ValueError
                            except:
                                print("Duración inválida. No se actualizó.")
                        
                        print("Canción editada correctamente.")
                        break
                    nodo = nodo.siguiente
                
                if not encontrado:
                    print("No se encontró la canción para editar.")

            elif opcion == "0":
                print("\n¡Hasta luego! Gracias por usar Codefy.")
                break

            elif opcion == "99": # Depuración
                print(f"Cola apunta a: {self.reproductor.lista.cola.dato if self.reproductor.lista.cola else 'None'}")
                print(f"Cabeza apunta a: {self.reproductor.lista.cabeza.dato if self.reproductor.lista.cabeza else 'None'}")


            else:
                print("Opción no válida.")

    def menu_navegacion(self):
        while True:
            print("\n" + "="*45)
            print("MENÚ DE REPRODUCCIÓN")
            print("="*45)
            print("="*45)
            actual = self.reproductor.obtener_actual()
            if actual:
                print(f"SONANDO: {actual}")
            else:
                print("(Ninguna canción seleccionada)")
            print("-" * 45)
            print("1. Siguiente canción")
            print("2. Canción anterior")
            print("3. Ir a la primera")
            print("4. Ir a la última")
            print("5. Reproducir por Criterio")
            print("6. Repetir Lista")
            print("0. Volver al menú principal")
            print("="*45)
            
            op = input("> Selecciona una opción: ")
            
            if op == "1":
                cancion = self.reproductor.siguiente()
                if cancion: print("Siguiente:", cancion)
                else: print("No hay siguiente canción (Fin de lista).")

            elif op == "2":
                cancion = self.reproductor.anterior()
                if cancion: print("Anterior:", cancion)
                else: print("No hay anterior canción (Inicio de lista).")

            elif op == "3":
                cancion = self.reproductor.ir_primera()
                if cancion: print("Primera:", cancion)
                else: print("Lista vacía.")

            elif op == "4":
                cancion = self.reproductor.ir_ultima()
                if cancion: print("Última:", cancion)
                else: print("Lista vacía.")

            elif op == "5":
                print("\n--- CRITERIOS DE REPRODUCCIÓN ---")
                print("1. Por Nombre")
                print("2. Por Artista")
                print("3. Por Género")
                print("4. Por Álbum")
                print("5. Por Año")
                crit_op = input("> Elige criterio: ")
                criterios = {'1': 'nombre', '2': 'artista', '3': 'genero', '4': 'album', '5': 'anio'}
                
                if crit_op in criterios:
                    valor = input(f"Ingrese {criterios[crit_op]}: ")
                    cancion = self.reproductor.reproducir_por(criterios[crit_op], valor)
                    if cancion: print("Reproduciendo:", cancion)
                    else: print("No se encontró ninguna coincidencia.")
                else:
                    print("Criterio inválido.")

            elif op == "6":
                cancion = self.reproductor.repetir_lista()
                if cancion: print("Reiniciando lista:", cancion)
                else: print("Lista vacía.")

            elif op == "0":
                break
            else:
                print("Opción no válida.")

reproductor_app = Reproductor("Mi Playlist")
reproductor_app.lista.insertar_final(Cancion("Imagine", "John Lennon", "Rock", "Imagine", 1971, "3:04"))
reproductor_app.lista.insertar_final(Cancion("Yesterday", "The Beatles", "Pop", "Help!", 1965, "2:05"))
reproductor_app.lista.insertar_final(Cancion("Bohemian Rhapsody", "Queen", "Rock", "A Night at the Opera", 1975, "5:55"))
reproductor_app.lista.insertar_final(Cancion("Billie Jean", "Michael Jackson", "Pop", "Thriller", 1982, "4:54"))

if __name__ == "__main__":
    InterfazConsola(reproductor_app).ejecutar()
