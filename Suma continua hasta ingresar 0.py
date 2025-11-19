# Suma continua hasta ingresar 0
suma = 0

print("Ingrese números (0 para terminar):")

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break
    
    if numero < 0:
        continue
    
    suma += numero

print("La suma total de números positivos es:", suma)