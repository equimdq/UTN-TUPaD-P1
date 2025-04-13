suma = 0
# Se inicializa la variable suma en 0

numero = int(input("Ingrese un numero entero (0 para finalizar): "))
# Se solicita al usuario que ingrese un número entero

while numero != 0:
    # Mientras el número ingresado no sea 0
    suma += numero
    # Se suma el número ingresado a la variable suma
    numero = int(input("Ingrese un numero entero (0 para finalizar): "))
    # Se solicita nuevamente un número entero al usuario
print("La suma de los números ingresados es:", suma)
# Se imprime el resultado de la suma