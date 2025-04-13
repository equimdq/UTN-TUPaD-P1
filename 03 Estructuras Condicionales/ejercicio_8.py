nombre = input("Ingrese su nombre: ") # se solicita el nombre al usuario

# Se le pide al usuario que elija una opción para formatear su nombre

print("Elija una opción:")
print("1: Nombre en mayúsculas")
print("2: Nombre en minúsculas")
print("3: Nombre con la primera letra mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

# se evalua la opción elegida por el usuario y se aplica el formato correspondiente
if opcion == "1":
    print(nombre.upper())  
elif opcion == "2":
    print(nombre.lower()) 
elif opcion == "3":
    print(nombre.title())  
else:
    print("Opción no válida.") # se informa al usuario que la opción elegida no es válida
