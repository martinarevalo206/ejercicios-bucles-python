# Imprime tres columnas de números según la tabla 4.11
cantidad_numeros = int(input("Ingrese la cantidad de números: "))

for numero in range(1, cantidad_numeros + 1):
    print(numero, "\t", numero * numero, "\t", numero * numero + numero)