# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

# Importamos la funcion reduce desde la libreria de python
from functools import reduce

def producto_valores(lista):

    # Aplicamos el producto de los valores con la función reduce
    resultado = reduce(lambda x,y: x * y, lista)
    return resultado

# Definimos la lista de numeros
lista_numeros = [2, 4, 8]

# Mostramos por consola
print(producto_valores(lista_numeros))