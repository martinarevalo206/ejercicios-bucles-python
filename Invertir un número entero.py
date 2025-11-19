# Invertir un número entero
numero = int(input("Ingrese un número entero: "))

original = numero
invertido = 0

if numero < 0:
    numero = abs(numero)
    es_negativo = True
else:
    es_negativo = False

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

if es_negativo:
    invertido = -invertido

print("Número original:", original)
print("Número invertido:", invertido)