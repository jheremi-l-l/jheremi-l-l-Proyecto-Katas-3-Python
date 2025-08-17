# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# Funcion para ver con que letra empieza.
def empieza_con_letra(palabra, letra):
    # Comparamos si el indice de la palabra es igual a la letra entonce devuelve la letra
    # Nos aseguramos que en caso de que el indice este vacío no haya error
    # Es sensible a mayusculas aplicando lower()
    comienzo_letra = len(palabra) > 0 and palabra[0].lower() == letra.lower()
    return comienzo_letra
   

# Funcion para filtar lista
def filtrar_palabras(lista, letra):
    # Aplicamos filter() para filtrar las palabras y con la función Lambda podemos pasar los dos argumentos
    # list() convierte en una lista filtrada
    resultado = list(filter(lambda palabra: empieza_con_letra(palabra, letra), lista))
    return resultado


# Lista dada
lista_compra = ["", "Atún", "Brocoli", "Tomate", "Arroz"]

salida = filtrar_palabras(lista_compra,"a")
print(salida)