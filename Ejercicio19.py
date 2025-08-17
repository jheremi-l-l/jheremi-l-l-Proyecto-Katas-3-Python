# Crea una función lambda que filtre los números impares de una lista dada.

# Funcion anónima impares
def impares(lista):
    
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return impares




lista_numeros = [1, 3, 4, 5, 6, 8, 7]
resultado = impares(lista_numeros)
print(f"El resultado de impares es:{resultado}")