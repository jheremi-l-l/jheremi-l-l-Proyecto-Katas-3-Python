# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

#Funcion Generar Frase
def generar_frase(frase):
    # Convertimos la frase en una lista de palabras.
    lista_palabras = frase.split()

    # Con map() iteramamos sobre la lista y con len nos devuelve la longitud en enteros de lista_palabras
    lista_longitud = list(map(len, lista_palabras))
    return lista_longitud


frase = "Hola Mundo de Asturias"
print(f"Resultado: {generar_frase(frase)}")
