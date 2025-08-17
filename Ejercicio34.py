# Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# Implementar el método quitar_rama para eliminar una rama en una posición específica.
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

# Creamos clase Arbol
class Arbol:

    # Método Constructor.
    def __init__(self):
        
        # Atributos
        self.tronco = 1
        self.ramas = []

      

    
    # Metodo Crecer Tronco
    def crecer_tronco(self):
        
        # Aumentar + 1 longitud
        self.tronco += 1

    # Método Nueva Rama
    def nueva_rama(self):
        
        # Agragamos nueva rama
        self.ramas.append(1)
    
    # Método Crecer Ramas
    def crecer_ramas(self):

        # Iteramos del de ramas, si existen se suma en + 1 la longitud de las ramas
        for rama in range(len(self.ramas)):
            self.ramas[rama] += 1 
    
    # Método Quitar Rama
    def quitar_rama(self, posicion):

        # Si la posicion se encuentra dentro de las ramas existentes se eleminan
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print(f"⚠️ No hay rama en la posición {posicion}.")

        


    #Método Información Arbol
    def info_arbol(self):

     return (
            f"🌳 Tronco: {self.tronco} unidades\n"
            f"🌿 Número de ramas: {len(self.ramas)}\n"
            f"📏 Longitudes de ramas: {self.ramas}"
        )


# INSTANCIAMOS

# Caso de uso:

#a. Crear un árbol.

mi_arbol = Arbol()

#b. Hacer crecer el tronco una unidad.

mi_arbol.crecer_tronco()

#c. Añadir una nueva rama.

mi_arbol.nueva_rama()

#d. Hacer crecer todas las ramas una unidad.

mi_arbol.crecer_ramas()

#e. Añadir dos nuevas ramas.

mi_arbol.nueva_rama()
mi_arbol.nueva_rama()


#f. Retirar la rama situada en la posición 2.

mi_arbol.quitar_rama(1)

#g. Obtener información sobre el árbol.
print(mi_arbol.info_arbol())

