# Diccionario con las consignas de los ejercicios
consignas = {
    "1": "# Ejercicio 1: Diccionario de precios de frutas\nCrea un diccionario con los precios de algunas frutas.",
    "2": "# Ejercicio 2: Actualización de precios de frutas\nModifica los precios de algunas frutas en el diccionario.",
    "3": "# Ejercicio 3: Lista de frutas sin precios\nGenera una lista que contenga únicamente los nombres de las frutas.",
    "4": "# Ejercicio 4: Agenda de contactos\nPermite almacenar y consultar números telefónicos.",
    "5": "# Ejercicio 5: Análisis de palabras en una frase\nMuestra las palabras únicas y su frecuencia.",
    "6": "# Ejercicio 6: Promedio de notas de alumnos\nCalcula el promedio de cada alumno a partir de sus notas.",
    "7": "# Ejercicio 7: Aprobados en parciales\nMuestra quién aprobó ambos parciales, solo uno o al menos uno.",
    "8": "# Ejercicio 8: Gestión de stock de productos\nPermite consultar y modificar el stock de productos.",
    "9": "# Ejercicio 9: Agenda de eventos\nPermite consultar y agregar eventos en días y horas específicas.",
    "10": "# Ejercicio 10: Capitales y países\nInvierte un diccionario de países y capitales.",
}

# muestra el menú de opciones

def mostrar_menu():
    print("\nMenú de opciones:")
    for i in range(1, 11):
        print(f"{i}. Ejercicio {i}")
    print("11. Salir")

# Inicia el programa mostrando el menú y esperando la selección del usuario
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-11): ")

# Verifica si la opción es válida y muestra la consigna del ejercicio si existe
    if opcion in consignas:
        print(f"\n{consignas[opcion]}")  # Muestra la consigna del ejercicio
        ejecutar = input("¿Desea ejecutar este ejercicio? (s/n): ").lower()
        if ejecutar != "s":
            continue  # Si el usuario elige "n", vuelve al menú

    if opcion == "1": # Ejercicio 1: Diccionario de precios de frutas
        precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} # Crea un diccionario con los precios de algunas frutas.
        precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}) # Agrega nuevas frutas al diccionario con sus precios
        print(precios_frutas)

    elif opcion == "2":
        precios_frutas.update({'Banana': 1300, 'Manzana': 1700, 'Melón': 2800}) # Actualiza los precios de algunas frutas
        print(precios_frutas)

    elif opcion == "3":
        frutas = list(precios_frutas.keys()) # Crea una lista con las claves del diccionario (las frutas)
        print(frutas)

    elif opcion == "4":
        contactos = {input("Nombre: "): input("Teléfono: ") for _ in range(5)} # Crea un diccionario con 5 contactos
        # Permite al usuario ingresar 5 contactos con su nombre y número de teléfono
        nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
        print(f"El número de {nombre_consulta} es: {contactos.get(nombre_consulta, 'No se encontró el contacto')}")

    elif opcion == "5":
        frase = input("Ingrese una frase: ")
        palabras = frase.split() # Divide la frase en palabras usando splitting por espacios
        frecuencia = {palabra: palabras.count(palabra) for palabra in palabras} # Crea un diccionario con la frecuencia de cada palabra
        print("Palabras únicas:", set(palabras))
        print("Frecuencia de cada palabra:", frecuencia)

    elif opcion == "6":
        datos_alumnos = {input("Nombre: "): tuple(float(input(f"Ingrese la nota {i+1}: ")) for i in range(3)) for _ in range(3)} # Permite ingresar los nombres de 3 alumnos y sus 3 notas
        for nombre, notas in datos_alumnos.items(): # Calcula el promedio de cada alumno
            print(f"{nombre}: {sum(notas) / len(notas):.2f}") # Muestra el promedio de cada alumno

    elif opcion == "7":
        aprobados_parcial1 = {'Jazmin', 'Nicolas', 'Juan', 'Maria', 'Pedro'}
        aprobados_parcial2 = {'Jazmin', 'Nicolas', 'Maria', 'Ana', 'Lucas'}
        print("Aprobaron ambos parciales:", aprobados_parcial1 & aprobados_parcial2) # Muestra quién aprobó ambos parciales
        print("Aprobaron solo uno:", aprobados_parcial1 ^ aprobados_parcial2) # Muestra quién aprobó solo uno de los parciales
        print("Total aprobados:", aprobados_parcial1 | aprobados_parcial2) # Muestra quién aprobó al menos uno de los parciales

    elif opcion == "8":
        stock_productos = {"Manzanas": 10, "Bananas": 20, "Naranjas": 15}
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            unidades = int(input("Ingrese la cantidad a agregar: ")) # Permite al usuario ingresar un producto y la cantidad a agregar al stock
            stock_productos[producto] += unidades # Si el producto ya existe, se actualiza su stock
        else:
            stock_productos[producto] = int(input("Ingrese la cantidad inicial de stock: ")) # Si el producto no existe, se agrega al diccionario con la cantidad inicial
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades") # Muestra el stock actualizado del producto

    elif opcion == "9":
        agenda = {("Lunes", "10:00"): "Reunión de equipo", ("Martes", "15:00"): "Llamada con cliente"} # Crea una agenda con eventos programados en días y horas específicas
        dia, hora = input("Ingrese el día: "), input("Ingrese la hora (HH:MM): ") # Permite al usuario ingresar un día y una hora para consultar un evento
        print(f"Evento programado: {agenda.get((dia, hora), 'No hay eventos programados')}")

    elif opcion == "10":
        paises_a_capitales = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Francia": "París"} # Crea un diccionario que relaciona países con sus capitales
        capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()} # Invierte el diccionario de países a capitales
        print(capitales_a_paises)

    elif opcion == "11":
        print("Saliendo...")
        break

    else:
        print("Opción inválida, intenta nuevamente.")