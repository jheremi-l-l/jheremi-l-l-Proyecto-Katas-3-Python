# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Listas de elementos
lista1 = [2,3,4,3]
lista2 = [5,3,2]

# Funcion anonima para sumar dos listas
# Si la longitud de los elementos es diferente la función map se encarga de sumar solo la lista con la misma longitud. No produce error.
sumatorio_listas = list(map(lambda x,y: x + y, lista1, lista2))

print(sumatorio_listas)
