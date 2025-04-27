def ejercicio_1():
    print("\nConsigna: Crear una lista con números del 1 al 100 múltiplos de 4 usando range")
    multiplos_4 = list(range(4, 101, 4)) # los rangos que se definen en la función range son: (inicio, fin, paso)
    print("Múltiplos de 4:", multiplos_4)

def ejercicio_2():
    print("\nConsigna: Crear una lista de 5 elementos y mostrar el penúltimo")
    Lista5 = ["mesa", "silla", "celular", "Escritorio", "computadora"]
    print("Penúltimo elemento:", Lista5[-2]) # El índice -2 se refiere al penúltimo elemento de la lista

def ejercicio_3():
    print("\nConsigna: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.")
    lista_vacia = []
    lista_vacia.append("Mar del Plata") # Agregando elementos a la lista vacía
    lista_vacia.append("El Chalten")
    lista_vacia.append("Puerto Iguazú")
    print("Lista con palabras:", lista_vacia)

def ejercicio_4():
    print("\nConsigna: Reemplazar el segundo y último valor de la lista 'animales' con las palabras 'loro' y 'oso', respectivamente. Imprimir la lista resultante por pantalla.")
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro" # Reemplaza el segundo valor
    animales[-1] = "oso" # Reemplaza el último valor. El índice -1 se refiere al último elemento de la lista y uso este metodo para que sea más flexible si la lista cambia de tamaño.
    print("Lista de animales:", animales)

def ejercicio_5():
    print("\nConsigna: Explicar lo que hace el siguiente programa.")
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))  # Elimina el número más grande de la lista
    print("Lista sin el máximo:", numeros)
    print("Explicación: El programa borra el número más grande de la lista previamente creada.")

def ejercicio_6():
    print("\nConsigna: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.")
    numeros = list(range(10, 31, 5))
    print("Lista de números: ", numeros)
    print("Los primeros dos números de la lista son:", numeros[:2])

def ejercicio_7():
    print("\nConsigna: Reemplazar los dos valores centrales (índices 1 y 2) de la lista 'autos' por dos nuevos valores cualesquiera.")
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["amarok", "ecosport"] # Reemplaza los valores en los índices 1 y 2
    print("Lista de autos:", autos)

def ejercicio_8():
    print("\nConsigna: Crear una lista vacía llamada 'dobles' y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.")
    dobles = []
    dobles.append(5 * 2) # Agrega el doble de 5
    dobles.append(10 * 2) # Agrega el doble de 10
    dobles.append(15 * 2) # Agrega el doble de 15
    print("Los dobles de 5, 10 y 15 son:", dobles, "respectivamente")

def ejercicio_9():
    print("\nConsigna: Dada la lista 'compras', agregar 'jugo' al tercer cliente, reemplazar 'fideos' por 'tallarines' en el segundo cliente, y eliminar 'pan' del primer cliente.")
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    print("Lista de compras original:", compras) # Imprimo la lista original para compararla con la modificada
    compras[2].append("jugo") # Agrega "jugo" a la lista de compras
    compras[1][1] = "tallarines" # Reemplaza "fideos" por "tallarines"
    compras[0].remove("pan") # Elimina "pan" de la lista de compras
    print("Lista de compras:", compras) # Imprime la lista de compras resultante

def ejercicio_10():
    print("\nConsigna: Elaborar una lista anidada llamada 'lista_anidada' con los siguientes elementos: 15, True, [25.5, 57.9, 30.6], False.")
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print("Lista anidada:", lista_anidada)

def correr_todos():
    print("\n--- Ejecutando todos los ejercicios ---")
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()
    ejercicio_9()
    ejercicio_10()

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ejecutar TODOS los ejercicios")
        print("2. Elegir un ejercicio para ejecutar")
        print("3. Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == '1':
            correr_todos()
        elif opcion == '2':
            ejercicio_num = input("¿Qué número de ejercicio querés ejecutar (1-10)?: ")
            if ejercicio_num == '1':
                ejercicio_1()
            elif ejercicio_num == '2':
                ejercicio_2()
            elif ejercicio_num == '3':
                ejercicio_3()
            elif ejercicio_num == '4':
                ejercicio_4()
            elif ejercicio_num == '5':
                ejercicio_5()
            elif ejercicio_num == '6':
                ejercicio_6()
            elif ejercicio_num == '7':
                ejercicio_7()
            elif ejercicio_num == '8':
                ejercicio_8()
            elif ejercicio_num == '9':
                ejercicio_9()
            elif ejercicio_num == '10':
                ejercicio_10()
            else:
                print("Ejercicio no válido.")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    menu()

