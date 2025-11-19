# Contar pares e impares
pares = 0
impares = 0

print("Ingrese números (0 para terminar):")

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")