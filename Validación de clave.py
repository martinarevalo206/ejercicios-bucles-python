# Validación de clave
clave_correcta = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave_ingresada = input("Ingrese la clave: ")
    
    if clave_ingresada == clave_correcta:
        print("¡Acceso permitido!")
        break
    else:
        intentos += 1
        restantes = max_intentos - intentos
        if restantes > 0:
            print(f"Clave incorrecta. Te quedan {restantes} intento(s)")
        else:
            print("Acceso denegado. Has agotado los intentos")