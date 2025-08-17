# Crea una función que calcule el cubo de un número dado mediante una función lambda.

# Definimos la funcion lambada que calcule el cubo de un numero
cubo_numero = lambda x: x**3

# Pedimos a usuario que introduzca un numero
numero = int(input("Introduzca un numero: "))
# Mostramos por pantalla el resultado
print(f"El cubo de {numero} es: {cubo_numero(numero)}")
