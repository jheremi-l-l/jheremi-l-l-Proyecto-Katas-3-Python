# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def cadena_a_lista(cadena):
    # Covertimos la cadena de texto en una lista
    lista_convertida = cadena.split()
    return lista_convertida

def filtrar_longitud(lista, numero):
    # Con la función anonima lambda obtenemos la palabra mayor que numero que itera en la lista
    # Lo convertimos en una la lista para que sea legible
    resultado = list(filter(lambda palabra: len(palabra) > numero,lista ))

    return resultado

# Pasamos una cadena de texto y la convertimos a una lista
detalles = "Hola como estas Jheremi"
lista_convertida = cadena_a_lista(detalles)

# Se filtra según la longitud de numero
lista_palabras = filtrar_longitud(lista_convertida, 5)
print(lista_palabras)
