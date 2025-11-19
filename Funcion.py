# Calcula la función f(x) = x³ + x² - 5 para x desde 0 hasta n
valor_x = int(input("Ingrese el máximo valor para x: "))

x = 0
while x <= valor_x:
    funcion = x * 3 + x * 2 - 5
    print(f"Para x = {x}, f(x) = {funcion}")
    x = x + 2