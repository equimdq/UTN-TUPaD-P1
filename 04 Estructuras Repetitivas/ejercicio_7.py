num_fin = int(input("Ingrese un número entero: ")) # Se solicita al usuario que ingrese un número entero

suma = 0 # Se inicializa la variable suma en 0
i = 0 # Se inicializa la variable i en 0
while i <= num_fin: # Mientras i sea menor o igual que num_fin
    suma += i
    i += 1

print("La suma de los números enteros desde 0 hasta", num_fin, "es:", suma)