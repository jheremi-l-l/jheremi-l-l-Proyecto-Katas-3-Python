# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
#         0 - 69: insuficiente
#         70 - 79: bien
#         80 - 89: muy bien
#         90 - 100: excelente


try:
    nota = int(input("Introduzca su nota para saber si es: (insuficiente, bien, muy bien, excelente): "))

    # Verificamos si las notas estan en cada rango para dar la solucion correspondiente
    if 0 <= nota <= 69:
        print("❌ Su nota es un Insuficiente")
    elif 70 <= nota <= 79:
        print("✅ Su nota es un Bien ")
    elif 80 <= nota <= 89:
        print("✅ Su nota es un Muy Bien ")
    elif 90 <= nota <= 100:
        print("✅ Su nota es un Excelente ")
except ValueError:
    print("❌ Entrada no valida. Introduzca números enteros")