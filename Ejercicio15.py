# Crea una función lambda que sume 3 a cada número de una lista dada.

def sumatorioa_a_3(lista):
    # La funcion lambda suma en 3 los numeros de la lista dada
    # Por medio de map podemos filtrar los elementos y lo convertimos en una lista con list()
    suma_a_3 =  list(map(lambda numero:  numero + 3, lista))

    return suma_a_3

listanumeros = [2, 3, 5]

# Resultado
print(sumatorioa_a_3(listanumeros))