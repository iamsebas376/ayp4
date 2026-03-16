canciones_sebas = {
    "Hotel California",
    "Bohemian Rhapsody",
    "Stairway to Heaven",
    "Imagine",
    "Like a Rolling Stone",
    "Smells Like Teen Spirit",
    "Hey Jude",
    "Billie Jean",
    "Sweet Child o' Mine",
    "Purple Haze"
}

canciones_milton = {
    "Hotel California",
    "Sweet Child o' Mine",
    "Hey Jude",
    "Psychosocial",
    "Duality",
    "Numb",
    "In the End",
    "Master of Puppets",
    "Chop Suey!",
    "Toxicity"
}

# Playlist en común
playlist_comun = canciones_sebas & canciones_milton
print("Canciones en común: ", playlist_comun)

# Playlist únicas de Sebas
playlist_unica_sebas = canciones_sebas - canciones_milton
print("Canciones únicas de Sebas: ", playlist_unica_sebas)

# Playlist únicas de Milton
playlist_unica_milton = canciones_milton - canciones_sebas
print("Canciones únicas de Milton: ", playlist_unica_milton)

# Playlist total
playlist_total = canciones_sebas | canciones_milton
print("Playlist total: ", playlist_total)
