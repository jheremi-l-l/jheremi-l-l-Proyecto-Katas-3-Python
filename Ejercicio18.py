# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre": "Ana", "edad": 18, "calificacion": 95},
    {"nombre": "Luis", "edad": 19, "calificacion": 85},
    {"nombre": "María", "edad": 20, "calificacion": 92},
    {"nombre": "Carlos", "edad": 21, "calificacion": 88},
    {"nombre": "Lucía", "edad": 22, "calificacion": 90}
]

# Usamos filter para obtener estudiante con nota >= 90
resultado = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

# Mostramos Resultados
# Usamos un for para mostrar por pantalla los resultados iterando los elementos de la lista.
for estudiante in resultado:
    print(f"Nombre Estudiante: {estudiante["nombre"]}, Edad: {estudiante["edad"]}, Calificación: {estudiante["calificacion"]}")
