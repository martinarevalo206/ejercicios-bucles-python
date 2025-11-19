# Permite repasar tablas de multiplicar con calificación
tabla = int(input("¿Qué tabla desea repasar (1-10)? "))
aciertos = 0

print(f"\nTabla del {tabla}:")

for i in range(1, 11):
    respuesta = int(input(f"{tabla} x {i} = "))
    resultado_correcto = tabla * i
    
    if respuesta == resultado_correcto:
        print("¡Correcto!")
        aciertos = aciertos + 1
    else:
        print(f"Incorrecto. La respuesta correcta es {resultado_correcto}")

# Calificación según la tabla
print(f"\nTotal de aciertos: {aciertos}")

if aciertos <= 5:
    print("Valoración: Insuficiente")
elif aciertos <= 7:
    print("Valoración: Aceptable")
elif aciertos <= 9:
    print("Valoración: Sobresaliente")
else:
    print("Valoración: Excelente")
    