# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_variable(variable):

    # Convertimos a cadena de texto la variable dada
    cadena = str(variable)

    
    # Enmascarado de la cadena

    # Si es menor o igual a 4 no se enmascara nada
    if len(cadena) <= 4:

        return cadena

    # Añadimos # a toda la cadena excepto los 4 ultimos.
    parte_enmascarada = "#" * (len(cadena) - 4)
    # Por indexacion recogemos los 4 ultimos elementos de la cadena
    cuatro_ultimos = cadena[-4:]

    return parte_enmascarada + cuatro_ultimos
    

dato = "Nuevalunamilenaria"
print(enmascarar_variable(dato))

    