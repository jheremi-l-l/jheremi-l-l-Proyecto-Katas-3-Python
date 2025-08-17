# Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# Importamos libreria reduce
from functools import reduce

def diferencia_total(lista):

    # Aplicamos el método reduce para calcular la diferencia total
    resultado = reduce(lambda x, y: x - y, lista)

    return resultado

lista_numeros = [2, 4 ,8]

print(diferencia_total(lista_numeros))