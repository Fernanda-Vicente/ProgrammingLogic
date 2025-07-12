import random

# Generar un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento != numero_secreto:
        print("Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
