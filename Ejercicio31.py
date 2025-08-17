# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.


def buscar_nombre():
    try:
        # Entrada de Usuario
        pedir_lista = str(input("Introduce una Lista de Nombres ej:(Ana, Maria, Luis...): "))
        
        # Lista vacia para almacenar los nombres  
        lista_nombres = []

        # Separamos por ","
        nombres = pedir_lista.split(",")

        # Iteramos en cada nombre indivudualmente

        for nombre in nombres:

            # Asignamos nombres sin espacios y sensible a mayusculas/minusculas
            nombre_limpio = nombre.strip().lower()
            lista_nombres.append(nombre_limpio)


        # Solicitud de nombre que quieres bucar
        nombre_buscar = input("Introduce el nombre a buscar: ").strip().lower()

        # Comprobamos que la lista está
        if nombre_buscar in lista_nombres:
            print(f"✅ El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"❌ El nombre '{nombre_buscar}' no está en la lista.")

    # Marcamos la excepción 
    except ValueError as e:
        print(e)

buscar_nombre()