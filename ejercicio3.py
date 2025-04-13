numero1 = int(input("Digite un número: "))
numero2 = int(input("Digite otro número: "))


if numero1 > numero2:
    numero1, numero2 = numero2, numero1 # Intercambiar los valores si el primero es mayor que el segundo

suma = 0
for i in range(numero1 + 1, numero2):
    suma += i

print("La suma de los números entre", numero1, "y", numero2, "es:", suma)
# El código solicita al usuario que ingrese dos números enteros y luego calcula la suma de los números entre ellos.