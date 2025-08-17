# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def nota_media(lista_notas, nota_aprobado=5):

    # Evaluamos si no hay notas para evitar divisiones por 0
    if lista_notas == []:
        return (None, "No hay notas para evuluar")
    # Nota media de las notas
    promedio = sum(lista_notas)/len(lista_notas)

    # Estado
    estado = "Aprobado" if promedio >= nota_aprobado else "Suspenso"

    # Tupla con nota media y estado = "Aprobado" o "Suspenso"
    return (promedio, estado)
    
# Lista de Notas
notas = [5,6,7,8]
notas_1 = [4,5,6,4]


resultado = nota_media(notas)
resultado1 = nota_media(notas_1)

print(f"Resultado final de la nota: {resultado}")
print(f"Resultado final de la nota: {resultado1}")
    


