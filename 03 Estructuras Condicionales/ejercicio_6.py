import random
from statistics import mode, median, mean

# Generar 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular media, mediana y moda
# La media es el promedio de los números
# La mediana es el valor medio cuando los números están ordenados
# La moda es el número que más se repite en la lista
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Muestra por pantalla los números generados y los resultados
print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Evalua el sesgo de la distribución
# La distribución tiene sesgo positivo si la media es mayor que la mediana y la mediana es mayor que la moda
# La distribución tiene sesgo negativo si la media es menor que la mediana y la mediana es menor que la moda
# La distribución no tiene sesgo si la media, mediana y moda son iguales
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("La distribución no tiene un sesgo claro según los criterios dados.")