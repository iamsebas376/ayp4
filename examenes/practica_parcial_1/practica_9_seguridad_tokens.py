# PRACTICA 9: SEGURIDAD DE TOKENS (JWT SIMPLE)
# TEMAS: REGEX CAPTURE GROUPS + SETS (Intersección de Permisos) + RECURSIVIDAD SIMPLE

import re

class SistemaSeguridad:
    def __init__(self):
        # Permisos requeridos para acciones críticas
        self.permisos_criticos = {"admin", "write", "delete"} # Set

    def extraer_datos_token(self, token):
        """UsaRegex con grupos de captura para extraer usuario y roles."""
        # Formato esperado: USER:identificador|ROLES:r1,r2,r3
        patron = r"^USER:(\w+)\|ROLES:([\w,]+)$"
        match = re.match(patron, token)
        
        if match:
            usuario = match.group(1)
            roles_lista = match.group(2).split(",")
            return usuario, set(roles_lista) # Retorna usuario y set de roles
        else:
            return None, None

    def tiene_permisos_rec(self, roles_usuario):
        """Verifica si el usuario tiene AL MENOS UN permiso crítico (Intersección)."""
        # INTERSECCIÓN: ¿Hay algo común entre roles_usuario y permisos_criticos?
        comunes = roles_usuario & self.permisos_criticos
        return len(comunes) > 0

    def validar_lista_tokens_rec(self, tokens):
        """Valida una lista de tokens de forma recursiva."""
        if not tokens:
            return []
        
        token_actual = tokens[0]
        user, roles = self.extraer_datos_token(token_actual)
        
        resultado = []
        if user:
            es_critico = self.tiene_permisos_rec(roles)
            resultado.append(f"Usuario: {user} | Crítico: {es_critico}")
        else:
            resultado.append(f"Token Inválido!")
            
        return resultado + self.validar_lista_tokens_rec(tokens[1:])

if __name__ == "__main__":
    seg = SistemaSeguridad()
    
    lista = [
        "USER:Sebas|ROLES:read,write",    # Válido + Crítico (write)
        "USER:Sofi|ROLES:read",          # Válido + No Crítico
        "Token Mal Formado",             # Inválido
        "USER:Admin|ROLES:admin,read"    # Válido + Crítico (admin)
    ]
    
    print("\n--- Resultados de Validación (Recursivo) ---")
    resultados = seg.validar_lista_tokens_rec(lista)
    for r in resultados:
        print(r)
