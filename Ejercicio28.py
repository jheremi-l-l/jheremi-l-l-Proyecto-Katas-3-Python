# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


def encontrar_duplicado(lista):
      
    elemento_duplicado = []
    # Iteramos la lista
    for elemento in lista:

        if elemento in elemento_duplicado:
            # Encontramos el primer elemento duplicado
            return elemento
        
        elemento_duplicado.append(elemento)

    return "No hay elementos duplicados"        

lista = [1, 3, 4, 1]

print(f"El primer elemento duplicado encontrado es: {encontrar_duplicado(lista)}")