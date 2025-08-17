# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):

    # Calculamos el promedio
    promedio = sum(lista) / len(lista)

    return promedio

lista_numeros = [4, 5, 7, 2]

# Mostramos por pantalla el resultado.
print(calcular_promedio(lista_numeros))

