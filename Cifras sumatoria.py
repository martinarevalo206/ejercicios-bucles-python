# Determina el número de cifras y su sumatoria si es positivo
numero = int(input("Ingrese un número entero: "))

if numero > 0:
    cantidad_cifras = len(str(numero))
    suma_cifras = sum(int(digito) for digito in str(numero))
    
    print(f"El número tiene {cantidad_cifras} cifra(s)")
    print(f"La suma de las cifras es: {suma_cifras}")
else:
    print("El número no es positivo")