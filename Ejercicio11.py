# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# Controlamos el bucle mientras sea True
while True:
    try:
    # Control de Excepciones - Ingreso Datos
        edad_usuario = int(input("Introduzca su Edad: "))
        if edad_usuario < 0 or edad_usuario > 120:
            print("Error edad, la edad introducida debe estar entre 0 y 120 años")
        else:
            print(f"la edad del Usuario es: {edad_usuario}")
        break
    except ValueError:
        print("Debe introducir valores númericos")