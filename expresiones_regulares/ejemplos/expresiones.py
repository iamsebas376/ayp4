import re

#Expresion regular de un correo electrónico

print("\nExpresión correo:")
def verificar_correo(correo):
    correo_valido = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo)
    return f"Correo {correo}:", bool(correo_valido)

print(verificar_correo("londonosebas201.sloa@gmail.com"))
print(verificar_correo("londonosebas201.sloa@gmail.com.co"))
print(verificar_correo("londonosebas201.sloa@@gmail.com"))

#Expresion digitos
# lista= ["hola", "estás", "123.", "5.2"]

# for i in lista:
#     if re.fullmatch(r"\d+(\.\d*)?", i):
#         print(f"{i} es un número")

# texto = "sol luna estrella cielo mar" 
# patron = r"\b[a-zA-Z]{3,5}\b"

# resultado = re.findall(patron, texto)
# print(resultado)

#Programa que reciba un texto y que el resultado sea cuales numeros están ahí
# texto = input("Ingrese un texto: ")
# texto = "estamos en el año 2025 y comenzamos el semestre 1 en el poli"
# resultado_texto = re.findall(r"\d+", texto)

# print("Números encontrados: ", resultado_texto)

# patron_contrasena = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_%]).{8,}$"
# resultado_contrasena = re.fullmatch(patron_contrasena, "nj%^jbXrS6g7Tna1-")
# print("Resultado contraseña: ", resultado_contrasena)

#Nombre de usuario que empieze por una letra mayúscula o minúscula que solo tenga 
#letras números o guiones bajos entre 5 y 15 carácteres

# nombre_usuario = input("Ingrese un nombre de usuario: ")
# patron_usuario = r"^[a-zA-Z][\w]{4,14}$"
# resultado_usuario = re.fullmatch(patron_usuario, nombre_usuario)

# if re.match(patron_usuario, nombre_usuario):
#     print("Nombre de usuario válido")
# else:
#     print("Nombre de usuario inválido")

# Expresión para validar el celular incluyendo guiones y espacios
print("\nExpresión celular:")
def validar_celular(numero):
    telefono_valido = re.match(r"^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$", numero)
    return f"Celular {numero}:", bool(telefono_valido)

print(validar_celular("310-601-1994"))
print(validar_celular("310 601 1994"))
print(validar_celular("3106011994"))

# Expresión para validar formato de una fecha
print("\nExpresión fecha:")
def validar_fecha(fecha):
    fecha_valida = re.match(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}$", fecha)
    return f"Fecha {fecha}:", bool(fecha_valida)

print(validar_fecha("09-01-2002"))
print(validar_fecha("19-12-2026"))
print(validar_fecha("29-10-1971"))
print(validar_fecha("31-12-1800"))

# Experesión para veriricar contraseña, minimo 8 carácateres, mayúsculas, minúsculas, dígitos y carácteres especiales
print("\nExpresión contraseña:")
def validar_contrasena(contrasena):
    contrasena_valida = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_%]).{8,}$", contrasena)
    return f"Contraseña {contrasena}:", bool(contrasena_valida)

print(validar_contrasena("nj%^jbXrS6g7Tna1-"))
print(validar_contrasena("nj%^jbXrS6g7Tna1-"))
print(validar_contrasena("nj%^jbxrs6g7tna1-"))

