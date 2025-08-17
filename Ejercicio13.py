# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# Definimos Función tupla mayusula y minuscula
def convertir_letra(letra):
    letra_mayuscula = letra.upper()
    letra_minuscula = letra.lower()

    return (letra_mayuscula, letra_minuscula)


def mayusculas_minusculas_unicas(cadena):
    # definimos una lista vacia para almacenar los elementos no repetidos
    letras_no_repetidas = []
    for letra in cadena:
        # Si letra es un caracter alphanumerico y la letra es minuscula y no este dentro de la lista nueva se añade a la lista nueva.
        # isalpha() es un método que verifica que los caracters son del alfabeto.
        if letra.isalpha() and letra.lower() not in letras_no_repetidas:
            letras_no_repetidas.append(letra.lower())
    
    # Aplicamos map() usando la funcion para convertir la cadena en mayusculas y minusculas
    lista_tuplas = list(map(convertir_letra, letras_no_repetidas))
    return lista_tuplas


palabra = "Hola Asturias que tal"
print(f"Resultado: {mayusculas_minusculas_unicas(palabra)}")
