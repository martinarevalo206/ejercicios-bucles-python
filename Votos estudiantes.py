# Encuesta para determinar la plataforma preferida
android = 0
ios = 0

estudiante = input("Ingrese el código del estudiante (Enter para terminar): ")

while estudiante != "":
    plataforma = input("Ingrese su elección (Android/iOS): ").lower()
    
    if plataforma == "android":
        android = android + 1
    elif plataforma == "ios":
        ios = ios + 1
    else:
        print("Opción no válida")
    
    estudiante = input("Ingrese el código del estudiante (Enter para terminar): ")

print(f"\nResultados de la votación:")
print(f"Android: {android} votos")
print(f"iOS: {ios} votos")

if android > ios:
    print("La plataforma ganadora es: Android")
elif ios > android:
    print("La plataforma ganadora es: iOS")
else:
    print("Hay un empate")