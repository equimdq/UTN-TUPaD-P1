numero = int(input("Ingrese un número par: "))
if numero % 2 == 0: # Con el operador módulo % verificamos si el número es par
    # Si el residuo de dividir el número entre 2 es cero, entonces es par
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")