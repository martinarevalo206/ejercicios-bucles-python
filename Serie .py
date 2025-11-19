# Genera e imprime la serie: 1, 3, 5, 7, 9, 11, ..., n
cantidad_terminos = int(input("Ingrese la cantidad de términos a generar: "))

termino = 1
contador = 1

while contador <= cantidad_terminos - 1:
    print(termino, end=", ")
    termino = termino + 2
    contador = contador + 1

print(termino)  # Último término sin coma