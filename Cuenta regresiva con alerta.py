# Cuenta regresiva con alerta
numero = int(input("Ingrese un número entero: "))

print("Cuenta regresiva:")

for i in range(numero, -1, -1):
    if i % 7 == 0:
        print(f"{i} ¡ALERTA! (múltiplo de 7)")
    else:
        print(i)