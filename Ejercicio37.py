# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# Controlamos erorres
try:
    hora = int(input("Introduce la hora en formato 24h (0-23): "))

    if 6 <= hora < 13:
        print("☀️ Es de día (mañana).")
    elif 13 <= hora < 20:
        print("🌇 Es de tarde.")
    elif 20 <= hora < 24 or 0 <= hora < 6:
        print("🌙 Es de noche.")
    else:
        print("❌ Hora inválida. Debe estar entre 0 y 23.")
except ValueError:
    print("❌ Entrada no válida. Por favor, introduce un número entero.")