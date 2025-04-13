numeros = 10 # Se define la cantidad de números a ingresar

suma = 0

contador = 1 # Se inicializa el contador en 1

while contador <= numeros:
    num = int(input(f"Ingrese el número {contador}: ")) # Se solicita al usuario que ingrese un número entero
    suma += num
    contador += 1

media = suma / numeros

print(f"La media de los números ingresados es: {media}") # Se imprime el resultado de la media