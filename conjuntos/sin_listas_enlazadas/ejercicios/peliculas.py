# Diccionario con peliculas, y su valor es un conjuntos de los generos asociados

catalogo = {
    "The Matrix": {"Ciencia Ficcion", "Accion"},
    "The Godfather": {"Crimen", "Drama"},
    "The Dark Knight": {"Accion", "Crimen", "Drama"},
    "Pulp Fiction": {"Crimen", "Drama"},
    "Forrest Gump": {"Drama", "Romance"},
    "Inception": {"Ciencia Ficcion", "Accion", "Thriller"},
    "The Lion King": {"Animacion", "Aventura", "Drama"},
    "The Matrix": {"Ciencia Ficcion", "Accion"},
    "The Godfather": {"Crimen", "Drama"},
    "The Dark Knight": {"Accion", "Crimen", "Drama"},
    "Pulp Fiction": {"Crimen", "Drama"},
    "Forrest Gump": {"Drama", "Romance"},
    "Inception": {"Ciencia Ficcion", "Accion", "Thriller"},
    "The Lion King": {"Animacion", "Aventura", "Drama"},
}

# Generos que existen
generos = set()
for pelicula in catalogo:
    generos.update(catalogo[pelicula])
print("\nGeneros que existen:", generos)

# Obtener peliculas similares (Al menos 2 generos en comun)

peliculas = list(catalogo.keys())
peliculas_comunes = []

for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        generos_comunes = catalogo[p1].intersection(catalogo[p2])
        if len(generos_comunes) >= 2:
            peliculas_comunes.append((p1, p2, generos_comunes))

print("\nPeliculas similares:", peliculas_comunes)