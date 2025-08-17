# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contador_caracteres(caracteres):
    # Iniciamos variables para contar los caracteres totales
    
    contador = 0
    # Iteramos sobre la variable de caracteres
    for caracter in caracteres:
        # Validacion de espacios si no hay espacios se suma 1 el contador para sino no se suma.
        if caracter != " ":
           contador += 1
    
    return contador
        
    

    # Otro método más rapido
    # return len(caracteres)

palabra = "Hola buenos dias"

print(contador_caracteres(palabra))

