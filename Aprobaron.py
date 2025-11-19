# Determina cuántos estudiantes aprobaron/reprobaron y el promedio general
codigo = int(input("Ingrese el código del estudiante (0 para terminar): "))
aprobados = 0
reprobados = 0
suma_notas = 0
total_estudiantes = 0

while codigo != 0:
    nota = float(input("Ingrese la nota del estudiante: "))
    
    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    
    suma_notas = suma_notas + nota
    total_estudiantes = total_estudiantes + 1
    
    codigo = int(input("Ingrese el código del estudiante (0 para terminar): "))

if total_estudiantes > 0:
    promedio = suma_notas / total_estudiantes
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")
    print(f"Promedio general del grupo: {promedio:.2f}")