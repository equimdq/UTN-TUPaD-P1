# Definición de funciones
def leer_entero_validado(mensaje):
    n = int(input(f"{mensaje}: "))
    # Validar que el número sea un entero positivo
    while n < 1:
        n = int(input(f"ERROR. {mensaje}"))
    return n

def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2) # sin usar el operador %

def es_multiplo (x, y):
    return obtener_resto(x, y) == 0 # sin usar el operador %

def sumatoria_de_divisores_propios(numero):
    sumatoria = 0  # Aquí se usa sumatoria, no suma
    for i in range (1, numero // 2 + 1):
        if es_multiplo(numero, i):
            sumatoria += i  # Se corrige el nombre de la variable
    return sumatoria
    

def es_perfecto(numero):
    return sumatoria_de_divisores_propios(numero) == numero


def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")


# Programa principal
num = leer_entero_validado ("Ingresa un número natural")
informar_si_numero_es_perfecto(num)
# print(f"seguimos adelante con el número {num}")