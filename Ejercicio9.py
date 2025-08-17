# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# Función para controlar las mascotas permitidas
def mascotas_permitidas(nombre_mascota):
    descartado = nombre_mascota not in lista_prohibida
    return descartado

    
#Función para filtrar las mascotas permitidas
def filtrar_mascotas(lista_mascotas):
    lista_filtrada = list(filter(mascotas_permitidas, lista_mascotas))
    return lista_filtrada


# Lista Prohibida
lista_prohibida = ["Mapache", "Tigre", "Serpiente", "Pitón", "Cocodrilo", "Oso"]
print(f"⛔ La lista Prohibida de Mascotas de la UE es: {lista_prohibida}\n")

# Lista de Mascotas
lista_mascotas_EU = ["Perro", "Tigre", "Serpiente", "Gato" , "Urón", "Oso"]

# Nueva lista Filtrada
resultado = filtrar_mascotas(lista_mascotas_EU)
print(f"✅ Tus mascotas permitidas son estas: {resultado}")



