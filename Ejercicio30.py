# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagrama(palabra1, palabra2):

    # Hacemos sensible las palabras a minusculas/mayusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Con el metodo sorted() ordenamos los elementos manteniendo el original

    return sorted(palabra1) == sorted(palabra2)

# Mostramos por pantalla
print(f"La palabras son Anagrama¿?: {anagrama("Roma", "amor")}")
print(f"La palabras son Anagrama¿?: {anagrama("Pincel", "Pernil")}")

