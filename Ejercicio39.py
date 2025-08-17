# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# Importamos libreria para realizar operaciones aritmeticas
import math


def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura
     
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    elif figura == "circulo":
        (radio) = datos
        return math.pi * radio ** 2
    else:
        return "❌ Figura no reconocida. Usa 'rectangulo', 'triangulo' o 'circulo'."



# Aplicamos el programa
print(calcular_area("prisma", (5, 3)))  
print(calcular_area("triangulo", (4, 6)))  
print(calcular_area("circulo", (7)))  