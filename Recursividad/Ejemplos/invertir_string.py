# Invertir String
# Hola --> aloH

def invertir_string(s):
    if len(s) <= 1:
        return s
    return invertir_string(s[1:]) + s[0]

print(invertir_string("Hola"))