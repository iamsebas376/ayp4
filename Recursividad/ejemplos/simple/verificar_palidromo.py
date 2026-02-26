# Verificar si la palabra es palíndroma
# reconocer --> reconocer

def verificar_palindromo(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return verificar_palindromo(s[1:-1])


print(verificar_palindromo("reconocer"))