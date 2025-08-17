# Crea una función lambda que calcule el resto de la división entre dos números dados.


resto_division = lambda x , y: x % y




# Evitamos Division por zero
# Pedimos numeros por Entrada
try:
    x = int(input("Introduce el primer número: "))
    y = int(input("Introduce el segundo número: "))

    print(resto_division(x,y))
except ZeroDivisionError:

    print("⚠️ Error: No se puede dividir entre cero.")

