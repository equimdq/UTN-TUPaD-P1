import math

print("Trabajo Práctico 5")
print("Nombre: Ventura, Ezequiel")
print("Eliga qué ejercicio desea ejecutar")
print("1) Ejercicio 1")
print("2) Ejercicio 2")
print("3) Ejercicio 3")
print("4) Ejercicio 4")
print("5) Ejercicio 5")
print("6) Ejercicio 6")
print("7) Ejercicio 7")
print("8) Ejercicio 8")
print("9) Ejercicio 9")
print("10) Ejercicio 10")
print("11) Todos")
print("12) Salir")

opcion = int(input("Ingrese su opción: "))

# -------------------- Ejercicio 1 --------------------
if opcion == 1 or opcion == 11:
    print("\nEjercicio 1")
    print("""Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.\n""")

# Definicion de funciones

    def imprimir_hola_mundo():
        print("Hola Mundo!")

# Programa principal

    imprimir_hola_mundo()

# -------------------- Ejercicio 2 --------------------
if opcion == 2 or opcion == 11:
    print("\nEjercicio 2")
    print("""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.\n""")

# Definicion de funciones

    def saludar_usuario(nombre):
        return f"Hola {nombre}!"

# Programa principal

    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

# -------------------- Ejercicio 3 --------------------
if opcion == 3 or opcion == 11:
    print("\nEjercicio 3")
    print("""Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
“Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.\n""")

# Definicion de funciones

    def informacion_personal(nombre, apellido, edad, residencia):
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

# -------------------- Ejercicio 4 --------------------
if opcion == 4 or opcion == 11:
    print("\nEjercicio 4")
    print("""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.\n""")

# Definicion de funciones

    def calcular_area_circulo(radio):
        return math.pi * radio ** 2

    def calcular_perimetro_circulo(radio):
        return 2 * math.pi * radio

# Programa principal

    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

# -------------------- Ejercicio 5 --------------------
if opcion == 5 or opcion == 11:
    print("\nEjercicio 5")
    print("""Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.\n""")

# Definicion de funciones

    def segundos_a_horas(segundos):
        return segundos / 3600

# Programa principal

    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# -------------------- Ejercicio 6 --------------------

if opcion == 6 or opcion == 11:
    print("\nEjercicio 6")
    print("""Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.\n""")

# Definicion de funciones

    def tabla_multiplicar(numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

# Programa principal

    numero = int(input("Ingrese un número: "))
    print(f"Tabla de multiplicar del {numero}:")
    tabla_multiplicar(numero)

# -------------------- Ejercicio 7 --------------------

if opcion == 7 or opcion == 11:
    print("\nEjercicio 7")
    print("""Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.\n""")

# Definicion de funciones

    def operaciones_basicas(a, b):
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b if b != 0 else "Error: División por cero"
        return (suma, resta, multiplicacion, division)
    
    # Programa principal

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

# -------------------- Ejercicio 8 --------------------

if opcion == 8 or opcion == 11:
    print("\nEjercicio 8")
    print("""Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. \n""")

# Definicion de funciones

    def calcular_imc(peso, altura):
        return peso / (altura ** 2)
    
# Programa principal

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# -------------------- Ejercicio 9 --------------------

if opcion == 9 or opcion == 11:
    print("\nEjercicio 9")
    print("""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.\n""")

# Definicion de funciones
    
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
# Programa principal
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

# -------------------- Ejercicio 10 --------------------

if opcion == 10 or opcion == 11:
    print("\nEjercicio 10")
    print("""Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función. \n""")

# Definicion de funciones
    def calcular_promedio(a, b, c):
        return (a + b + c) / 3
    
# Programa principal
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

