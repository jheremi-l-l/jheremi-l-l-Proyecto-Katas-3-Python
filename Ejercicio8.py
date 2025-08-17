# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

def division_dos_numeros(num1, num2):
     # Divison de 2 numeros
        resultado = num1 / num2
        return resultado
    
# Datos Pedidos a Usuario
  # Controlamos las Excepciones
try:
    numero1 = float(input("Ingrese el numero 1: \n"))
    numero2 = float(input("Ingrese el numero 2: \n"))
    solucion = division_dos_numeros(numero1, numero2)
    print(f"Solucion de la Division: {round(solucion,2)}")
except ValueError:# En caso que el usuario Ingrese letras 
        print("Por favor, Ingrese sólo numeros.")
except ZeroDivisionError:# En caso que el usuario ingrese un Divisor 0
        print("Ingrese Numero Válido")
