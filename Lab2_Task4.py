# Diccionario con las calificaciones de los estudiantes
estudiantes = {
    "Ana": [85, 90, 78, 92, 88],
    "Carlos": [76, 82, 80, 85, 79],
    "María": [95, 98, 92, 96, 94],
    "Juan": [70, 75, 72, 68, 74],
    "Sofía": [88, 85, 90, 87, 89]
}

print("=== CALIFICACIONES ORIGINALES ===")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

# Crear nuevo diccionario con promedios
promedios = {}

for nombre, calificaciones in estudiantes.items():
    # Calcular el promedio usando sum()
    suma_total = sum(calificaciones)
    cantidad_materias = 0
    
    # Contar cantidad de materias sin usar len()
    for _ in calificaciones:
        cantidad_materias = cantidad_materias + 1
    
    # Calcular promedio
    promedio = suma_total / cantidad_materias
    
    # Agregar al nuevo diccionario
    promedios[nombre] = promedio

print("=== DICCIONARIO DE PROMEDIOS ===")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")