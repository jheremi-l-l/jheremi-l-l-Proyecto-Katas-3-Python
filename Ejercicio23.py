# Concatena una lista de palabras. Usa la función reduce().

# Añadimos la libreria reduce()
from functools import reduce

def concatenar_palabras(lista):

    # Validamos en caso de tener una lista vacía
    if not lista:
        return "La lista esta vacía"
    else:
        
        # Con la función reduce() concatenamos los elementos de la lista
        resultado = reduce(lambda x,y: x + " " + y , lista)
        return resultado
    
palabras = ["Lista", "Ordenada", "Mayor", "a", "Menor"]

print(concatenar_palabras(palabras))
