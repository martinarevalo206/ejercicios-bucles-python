# Serie Fibonacci hasta N
n = int(input("Ingrese el valor de N: "))

a, b = 0, 1

print("Serie de Fibonacci hasta", n)

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

print()
