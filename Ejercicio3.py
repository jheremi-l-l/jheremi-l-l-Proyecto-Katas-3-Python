# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# Función para verificar si lalista contiene palabra: objetivo
def contiene_palabra(palabra, palabra_objetivo):
    if palabra_objetivo.lower() in palabra.lower(): # Nos aseguramos que las palabras esten en minusculas.
        return palabra_objetivo
    
# Función para filtrar la lista de palabras
def listado_completo(lista, palabra_objetivo):
    #Nueva lista para recoger las lista filtrada
    lista_filtrada = []
    # Iteramos la lista y añadimos 1 a 1 las coincidencias
    for palabra in lista:
        if contiene_palabra(palabra, palabra_objetivo):
            lista_filtrada.append(palabra)
    return lista_filtrada

# Lista de palabras
lista_palabras = ["Arroz", "Melon", "Harina", "Huevos revueltos", "Tortilla de Huevos", "Arroz con Bogavante"]
print(f"Lista Original: {lista_palabras}")

# Buscamos coincidencias con la palabra "Arroz"
nueva_lista = listado_completo(lista_palabras, "Arroz")
print(f"Nueva Lista con coincidencias: {nueva_lista}")


### Solución con una funcion labmda ###

def listado_completo_lambda(lista, palabra_objetivo):
    lista_filtrada = list(filter(lambda x: palabra_objetivo.lower() in x.lower(), lista))
    return lista_filtrada

# Listado de palabras que contenga palabra Objetivo = "Huevos"
nuevo_listado = listado_completo_lambda(lista_palabras, "Huevos")

print(f"Nueva Lista Lambda con coincidencias: {nueva_lista}")

