# Calcula el factorial de un número entero
numero = int(input("Ingrese un número entero: "))

if numero < 0:
    print("Los números negativos no tienen factorial")
elif numero == 0:
    print("0! = 1")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"{numero}! = {factorial}")
    