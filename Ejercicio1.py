# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def dict_letra(cadena_texto):
    # Creamos un diccionario vacio
    letra_cadena = {}
    
    # Recorremos cada letra de la cadena
    for letra in cadena_texto.lower(): # En caso de que se escriban mayusculas se cuenta tambien cada letra.
        if letra != " ": # Filtramos los espacios

            if letra in letra_cadena:
                letra_cadena[letra] += 1 # Si la letra ya esta en el diccionario se suma + 1
            else: 
                letra_cadena[letra] = 1 # Si no esta la letra es 1

    return letra_cadena

print(dict_letra("Perro perruno"))