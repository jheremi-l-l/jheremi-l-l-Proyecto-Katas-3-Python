# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

# Importamos la funcion reduce desde la libreria de python
from functools import reduce 

def lista_digitos(lista):
    # Con la funcion reduce y la funcion lambda multiplicamos el numero de la lista *10 y sumas el resultado al numero siguiente
    # Ej --> 2 *10 = 20 + 4 = 24 y 24 * 10 = 240 + 3
    resultado = reduce(lambda x,y: x*10 + y, lista)
    return resultado


lista_numeros = [2,4,3]
solucion = lista_digitos(lista_numeros)
print(solucion)
