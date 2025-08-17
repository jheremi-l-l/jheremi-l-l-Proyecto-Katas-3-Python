# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# Función para devolver el doble de un número
def doble_num(num):
    return num*2

# Creamos una lista con los numeros 
lista_numeros = [1, 2, 4, 6, 8]

# Aplicamos la funcion map para calcular el doble de cada valor en una nueva lista
lista_resultado_map = list(map(doble_num,(lista_numeros)))


# Salida por pantalla
print(f"El doble de cada número de la lista es: {lista_resultado_map}")

# Si se quiere hacer mediante el uso de lambdas
numeros = [1, 2, 3, 4, 5]
resultado_map_lambda = list(map(lambda x: x*2,numeros))
print(f"El resultado de la función map usando lambda es: {resultado_map_lambda}")