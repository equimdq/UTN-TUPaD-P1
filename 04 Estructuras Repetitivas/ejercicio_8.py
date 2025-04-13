# cantidad de números a ingresar
numeros = 10

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
contador = 1
while contador <= numeros:
    num = int(input(f"Ingresá el número {contador}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1


    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    contador += 1
# se muestran los resultados
print("Resultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
