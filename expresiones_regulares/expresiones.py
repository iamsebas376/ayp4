import re

#Expresion regular de un correo electrónico
resultado_correo = re.findall(r"^[\w\.-_]+@[a-zA-Z\.-]+\.[a-zA-Z]{2,}$", "londonosebas201.sloa@gmail.com.co")
print("Restultado correo: ",resultado_correo)

#Expresion digitos
lista= ["hola", "estás", "123.", "5.2"]

for i in lista:
    if re.fullmatch(r"\d+(\.\d*)?", i):
        print(f"{i} es un número")

texto = "sol luna estrella cielo mar" 
patron = r"\b[a-zA-Z]{3,5}\b"

resultado = re.findall(patron, texto)
print(resultado)

#Programa que reciba un texto y que el resultado sea cuales numeros están ahí
# texto = input("Ingrese un texto: ")
texto = "estamos en el año 2025 y comenzamos el semestre 1 en el poli"
resultado_texto = re.findall(r"\d+", texto)

print("Números encontrados: ", resultado_texto)

patron_contrasena = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_%]).{8,}$"
resultado_contrasena = re.fullmatch(patron_contrasena, "nj%^jbXrS6g7Tna1-")
print("Resultado contraseña: ", resultado_contrasena)

#Nombre de usuario que empieze por una letra mayúscula o minúscula que solo tenga 
#letras números o guiones bajos entre 5 y 15 carácteres

nombre_usuario = input("Ingrese un nombre de usuario: ")
patron_usuario = r"^[a-zA-Z][\w]{4,14}$"
resultado_usuario = re.fullmatch(patron_usuario, nombre_usuario)

if re.match(patron_usuario, nombre_usuario):
    print("Nombre de usuario válido")
else:
    print("Nombre de usuario inválido")