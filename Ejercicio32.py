# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre, empleados):

    # Iteramos sobre la lista de los empleados
    for empleado in empleados:

        # Si el empleado esta dentro de la lista lo retornamos
        if empleado["nombre"].lower() == nombre.lower():

            return f"✅ {nombre} trabaja como {empleado['puesto']}."
    
    # Solo se ejecuta si no se encuentra ningún empleado
    return f"❌ {nombre} no trabaja aquí."

        
# Lista de empleados como diccionarios
lista_empleados = [
    {"nombre": "Ana López", "puesto": "Diseñadora gráfica"},
    {"nombre": "Luis García", "puesto": "Desarrollador backend"},
    {"nombre": "Jheremi Lema", "puesto": "Analista de datos"},
    {"nombre": "Marta Ruiz", "puesto": "Gerente de proyectos"}
]

# Resultado Búsqueda.
print(buscar_empleado("Jheremi Lema", lista_empleados))
print(buscar_empleado("Marcos Pérez", lista_empleados))




