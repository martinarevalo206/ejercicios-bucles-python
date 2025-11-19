# Genera la serie: 1, 3, 5, 7, 9, 11, ..., n
n = int(input("Ingrese la cantidad de términos de la serie: "))

termino = 1
for i in range(n):
    print(termino, end=" ")
    termino = termino + 2