# Determinar si un número es primo
import math

numero = int(input("Ingrese un número entero mayor que 1: "))

if numero < 2:
    print(numero, "no es primo")
elif numero == 2:
    print(numero, "es primo")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")