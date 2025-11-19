# Determina si un número es de Armstrong
numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    n = len(str(numero))  # Cantidad de cifras
    suma = sum(int(digito) ** n for digito in str(numero))
    
    if suma == numero:
        print(f"{numero} ES un número de Armstrong")
    else:
        print(f"{numero} NO es un número de Armstrong")
else:
    print("Debe ingresar un número positivo")