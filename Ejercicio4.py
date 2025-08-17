# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def calcular_diferencia(lista1, lista2):
    # Aplicamos la resta entre cada par de los elementos de las 2 listas. Con la funcion map podemos manejar 2 o más listas
    listado_diferencia = list(map(lambda a, b: a - b, lista1, lista2))
    return listado_diferencia

#Lista 1
lista_num1=[4,1,4,3]

# Lista 2
lista_num2=[1,3,2]


resultado_lista = calcular_diferencia(lista_num1,lista_num2)
print(resultado_lista)

 # En caso de ser Longitudes diferentes de listas solo se aplicara la diferencia entre la misma logitud de la lista, map() se encarga de ello y no imprime ningun error.