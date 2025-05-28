import math  # importando la librería math para funciones matemáticas

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return suma, resta, multiplicacion, division

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def mostrar_menu():
    print("\nTrabajo Práctico 5")
    print("Nombre: Ventura, Ezequiel")
    print("Eliga cuál de los 10 ejercicios desea ejecutar:")
    print("Ingrese un número del 1 al 10, 11 para ejecutar todos o 12 para salir.")

def ejecutar_opcion(opcion):
    if opcion == 1 or opcion == 11:
        print("\nEjercicio 1")
        imprimir_hola_mundo()

    if opcion == 2 or opcion == 11:
        print("\nEjercicio 2")
        nombre = input("Ingrese su nombre: ")
        print(saludar_usuario(nombre))

    if opcion == 3 or opcion == 11:
        print("\nEjercicio 3")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = input("Ingrese su edad: ")
        residencia = input("Ingrese su residencia: ")
        informacion_personal(nombre, apellido, edad, residencia)

    if opcion == 4 or opcion == 11:
        print("\nEjercicio 4")
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"Área: {calcular_area_circulo(radio):.2f}")
            print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
        except ValueError:
            print("Entrada inválida.")

    if opcion == 5 or opcion == 11:
        print("\nEjercicio 5")
        try:
            segundos = int(input("Ingrese la cantidad de segundos: "))
            print(f"{segundos} segundos = {segundos_a_horas(segundos):.2f} horas")
        except ValueError:
            print("Entrada inválida.")

    if opcion == 6 or opcion == 11:
        print("\nEjercicio 6")
        try:
            numero = int(input("Ingrese un número: "))
            tabla_multiplicar(numero)
        except ValueError:
            print("Entrada inválida.")

    if opcion == 7 or opcion == 11:
        print("\nEjercicio 7")
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            suma, resta, mult, div = operaciones_basicas(a, b)
            print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {mult}\nDivisión: {div}")
        except ValueError:
            print("Entrada inválida.")

    if opcion == 8 or opcion == 11:
        print("\nEjercicio 8")
        try:
            peso = float(input("Peso en kg: "))
            altura = float(input("Altura en m: "))
            print(f"IMC: {calcular_imc(peso, altura):.2f}")
        except ValueError:
            print("Entrada inválida.")

    if opcion == 9 or opcion == 11:
        print("\nEjercicio 9")
        try:
            celsius = float(input("Temperatura en Celsius: "))
            print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")
        except ValueError:
            print("Entrada inválida.")

    if opcion == 10 or opcion == 11:
        print("\nEjercicio 10")
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            c = float(input("Tercer número: "))
            print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
        except ValueError:
            print("Entrada inválida.")

# Programa principal
while True:
    mostrar_menu()
    try:
        opcion = int(input())  # Solo se solicita una vez
        if opcion == 12:
            print("¡Gracias por usar el programa!")
            exit()  # Se termina el programa sin usar break
        elif 1 <= opcion <= 11:
            ejecutar_opcion(opcion)
        else:
            print("Opción inválida. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número válido.")