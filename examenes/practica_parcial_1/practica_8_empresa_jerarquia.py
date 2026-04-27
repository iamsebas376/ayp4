# PRACTICA 8: JERARQUÍA DE EMPRESA Y PRESUPUESTO
# TEMAS: RECURSIVIDAD DE ÁRBOL + CONJUNTOS DE DEPARTAMENTOS + LISTAS DE SUBORDINADOS

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.equipo = [] # Lista de otros objetos Empleado (Subordinados)

class Empresa:
    def __init__(self, jefe_maximo):
        self.ceo = jefe_maximo
        self.categorias = set() # Set de cargos únicos encontrados

    def calcular_presupuesto_total_rec(self, actual):
        """Calcula el costo total de salarios de un empleado y todo su equipo (árbol)."""
        if actual is None:
            return 0
        
        # Registrar cargo
        self.categorias.add(actual.cargo.lower())
        
        # Salario actual + Suma recursiva de todo su equipo
        total_equipo = 0
        for subordinado in actual.equipo:
            total_equipo += self.calcular_presupuesto_total_rec(subordinado)
            
        return actual.salario + total_equipo

    def buscar_por_nombre_rec(self, actual, nombre_objetivo):
        """Busca recursivamente a un empleado en toda la red jerárquica."""
        if actual is None: return None
        if actual.nombre.lower() == nombre_objetivo.lower():
            return actual
        
        for sub in actual.equipo:
            encontrado = self.buscar_por_nombre_rec(sub, nombre_objetivo)
            if encontrado: return encontrado
            
        return None

if __name__ == "__main__":
    # Creamos estructura
    juan = Empleado("Juan", "CEO", 5000)
    seba = Empleado("Seba", "Manager", 3000)
    sofa = Empleado("Sofa", "Manager", 3000)
    paco = Empleado("Paco", "Dev", 1500)
    pepe = Empleado("Pepe", "Dev", 1500)
    luis = Empleado("Luis", "QA", 1200)
    
    # Asignar jerarquía
    juan.equipo = [seba, sofa] # Seba y Sofa dependen de Juan
    seba.equipo = [paco, pepe] # Paco y Pepe dependen de Seba
    sofa.equipo = [luis]       # Luis depende de Sofa
    
    emp = Empresa(juan)
    
    print(f"Presupuesto Total Mensual: ${emp.calcular_presupuesto_total_rec(juan)}")
    print(f"Cargos registrados (Set): {emp.categorias}")
    
    # Búsqueda recursiva profunda
    obj = emp.buscar_por_nombre_rec(juan, "Luis")
    if obj:
        print(f"Emplado encontrado: {obj.nombre} trabaja como {obj.cargo}")
