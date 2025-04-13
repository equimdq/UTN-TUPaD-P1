import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1

# inicia el bucle para adivinar el número
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número entre 0 y 9: "))
    if adivinanza == numero_secreto:
        print("¡Correcto!")
    else:
        print("Incorrecto, intenta de nuevo.")
    # Se incrementa el contador de intentos
    intentos += 1

print("Adivinaste el número secreto!, el número era", numero_secreto)
print("Lo lograste en", intentos, "intento(s)")
print("Fin del juego")

