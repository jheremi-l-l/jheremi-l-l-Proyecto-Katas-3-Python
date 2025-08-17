# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Excepción Personalizada
class ListaVaciaError(Exception):
    pass

# Calculamos promedio de la lista
def calcular_promedio(lista):
    # Evaluamos la lista
    if not lista:
        # raise ejecuta la excepcion de forma explicita
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía")
    
    return sum(lista)/len(lista)


# Peticion de la lista con control de errores
try:
    # Definimos la lista de numeros
    lista_numeros = []
    lista_numeros2 = [4,5,7,8]

    resultado = calcular_promedio(lista_numeros)
    # resultado2 = calcular_promedio(lista_numeros2)
    print(resultado)
    # print(f"El primedio de la lista es: {resultado2}")
    
except ListaVaciaError as error:
    print(f"⚠️  Error: {error}")
    