# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def coversor_tupla_string(lista_tupla):
    # list() convierte el map en una Lista
    conversor = list(map(lambda x: " ".join(map(str, x)),lista_tupla)) # Con la funcion Lambda convertimos cada elemento x a string y .join() Une los elementos con espacio
    return conversor


# Segunda Solución sin función Lambda
def tupla_a_string(tupla):
    convertido = " ".join(map(str,tupla))
    return convertido

def lista_tupla_a_strig(lista_tupla):
    conversor = list(map(tupla_a_string, lista_tupla))
    return conversor

# Lista de tuplas
lista = [(2,3) , (5,7)]

# Salida Función Lambda
string_convertido = coversor_tupla_string(lista)
print(f"Solución 1: {string_convertido}")


# Salida Función Definida
print(f"Solucion 2: {lista_tupla_a_strig(lista)}")

