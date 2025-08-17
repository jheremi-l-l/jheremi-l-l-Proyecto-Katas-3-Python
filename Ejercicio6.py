# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    # Calculo Factorial
    if numero == 0  or numero == 1:
        return 1
    # Uso de la funcion recursiva par calcular su factorial.
    factorial_num = numero * factorial(numero - 1)
    return factorial_num

resultado = factorial(4)

print(f"Resultado Factorial: {resultado}")




