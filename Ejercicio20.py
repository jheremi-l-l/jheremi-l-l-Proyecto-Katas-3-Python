# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

# Lista dada
lista_combinada = [1, "1", "1", "Hola", 3]

# Filtramos con la funcion Lambda los enteros y con isinstace() verificamos que x que es un entero está dentro de la lista dada
solo_enteros = list(filter(lambda x: isinstance(x, int), lista_combinada))

print(solo_enteros)