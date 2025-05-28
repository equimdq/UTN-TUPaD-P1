def factorial_recursivo(n): # Función recursiva para calcular el factorial de un número
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def fibonacci_recursivo(posicion): # Función recursiva para calcular el valor de la serie de Fibonacci en una posición dada
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def potencia(base, exponente): # Función recursiva para calcular la potencia de un número base elevado a un exponente
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)

def convertir_a_binario(n): # Función recursiva para convertir un número entero a su representación binaria
    if n < 0:
        return "-" + convertir_a_binario(-n)
    elif n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return convertir_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra): # Función recursiva para verificar si una palabra es un palíndromo
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def suma_digitos(n): # Función recursiva para sumar los dígitos de un número
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n): # Función recursiva para contar el total de bloques necesarios para construir una pirámide
    if n <= 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_digito(numero, digito): # Función recursiva para contar cuántas veces aparece un dígito en un número
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        resto = numero // 10
        if ultimo == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return contar_digito(resto, digito)
        
# Programa principal

def menu(): # Función para mostrar el menú y ejecutar las opciones seleccionadas
    while True:
        print("\n--- Menú de ejercicios recursivos ---")
        print("1 - Factoriales del 1 al número dado")
        print("2 - Serie de Fibonacci hasta la posición dada")
        print("3 - Potencia de un número base elevado a un exponente")
        print("4 - Convertir número entero a binario")
        print("5 - Verificar si una palabra es palíndromo")
        print("6 - Suma de los dígitos de un número")
        print("7 - Total de bloques para construir una pirámide")
        print("8 - Contar cuántas veces aparece un dígito en un número")
        print("0 - Salir")

        opcion = input("Ingrese el número del ejercicio que desea ejecutar (0 para salir): ")

        if opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        elif opcion == "1":
            numero = int(input("Introduce un número entero positivo: "))
            if numero < 0:
                print("El número debe ser positivo.")
            else:
                print(f"\nFactoriales del 1 al {numero}:")
                for i in range(1, numero + 1):
                    print(f"{i}! = {factorial_recursivo(i)}")

        elif opcion == "2":
            posicion = int(input("Introduce una posición en la serie de Fibonacci: "))
            if posicion < 0:
                print("La posición debe ser un número entero no negativo.")
            else:
                print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
                for i in range(posicion + 1):
                    print(f"Posición {i}: {fibonacci_recursivo(i)}")

        elif opcion == "3":
            base = float(input("Introduce la base: "))
            exponente = int(input("Introduce el exponente: "))
            resultado = potencia(base, exponente)
            print(f"{base} elevado a {exponente} es {resultado}")

        elif opcion == "4":
            numero = int(input("Introduce un número entero para convertir a binario: "))
            binario = convertir_a_binario(numero)
            print(f"El número {numero} en binario es: {binario}")

        elif opcion == "5":
            texto = input("Introduce una palabra o frase sin espacios ni tildes: ").lower()
            if texto == "":
                print("Error: La entrada no puede estar vacía.")
            else:
                if es_palindromo(texto):
                    print(f"'{texto}' es un palíndromo.")
                else:
                    print(f"'{texto}' no es un palíndromo.")

        elif opcion == "6":
            numero = int(input("Introduce un número entero positivo: "))
            if numero < 0:
                print("Error: El número debe ser positivo.")
            else:
                resultado = suma_digitos(numero)
                print(f"La suma de los dígitos de {numero} es {resultado}")

        elif opcion == "7":
            n = int(input("Introduce el número de bloques en el nivel más bajo de la pirámide: "))
            if n < 1:
                print("Error: El número de bloques debe ser al menos 1.")
            else:
                total_bloques = contar_bloques(n)
                print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")

        elif opcion == "8":
            numero = int(input("Introduce un número entero positivo: "))
            digito = int(input("Introduce el dígito a buscar (0-9): "))
            if numero < 0 or digito < 0 or digito > 9:
                print("Error: Número debe ser positivo y dígito entre 0 y 9.")
            else:
                cantidad = contar_digito(numero, digito)
                print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

        else:
            print("Opción inválida. Por favor, ingresa un número entre 0 y 8.")

if __name__ == "__main__":
    menu()
