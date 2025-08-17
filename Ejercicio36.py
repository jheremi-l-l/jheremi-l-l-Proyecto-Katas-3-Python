# Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
def contar_palabras(texto):

    # Convertimos el texto en elementos
    palabras = texto.split()
    # Diccionario vacio par almacenar los elementos
    contador = {}

    # Recorremos cada palabra de la lista palabras
    for palabra in palabras:
        # Controlamos mayusculas y minisculas
        # Eliminamos caracteres especiales que se puedan introducir
        palabra_normalizada = palabra.lower().strip(".,;:!?¡¿()[]{}")

        # Con el método get() nos encargamos de controlar los elementos del diccionario
        # Si ya existe el elemento se suma uno +1 y sino devuelve 0
        contador[palabra_normalizada] = contador.get(palabra_normalizada, 0) + 1
    
    return contador


# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):

    texto_nuevo =  texto.replace(palabra_original, palabra_nueva)

    return texto_nuevo


# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
def eliminar_palabra(texto, palabra_a_eliminar):

    # Convertimos el texto en una lista
    palabras = texto.split()
    # Controlamos minusculas y mayusculas y los signos de puntuacion 
    palabra_a_eliminar = palabra_a_eliminar.lower().strip(".,;:!?¡¿()[]{}")


    # Aplico una lista de compresion para generar una lista con las palabras que sean distintas a la palabra a eliminar.
    eliminada = [
        palabra for palabra in palabras
        if palabra.lower().strip(".,;:!?¡¿()[]{}") != palabra_a_eliminar.lower()
    ]
    # Devolvemos una lista de palabras separadas por espacios
    return " ".join(eliminada)


# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

def procesar_texto(texto, opcion, *args):

    match opcion:
        case "contar":
            return contar_palabras(texto)
        case "reemplazar":
            # Validamos el uso de los Argumentos
            if len(args) != 2:
                raise ValueError("❌ Se requieren dos argumentos: palabra_original y palabra_nueva.")
            return reemplazar_palabras(texto, args[0], args[1])
        case "eliminar":
            # Validamos el uso de los Argumentos
            if len(args) != 1:
                raise ValueError("❌ Se require un argumento: palabra_a_eliminar")
            return eliminar_palabra(texto, args[0])
        case _:
            raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

        

# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.

texto = "Hola mundo, hola universo. El mundo es grande y el universo también."

# Contar palabras
print("🔢 Conteo de palabras:")
print(procesar_texto(texto, "contar"))

# Reemplazar palabra
print("\n🔁 Reemplazo de 'mundo' por 'planeta':")
print(procesar_texto(texto, "reemplazar", "mundo", "planeta"))

# Eliminar palabra
print("\n🗑️ Eliminación de la palabra 'universo':")
print(procesar_texto(texto, "eliminar", "universo"))
