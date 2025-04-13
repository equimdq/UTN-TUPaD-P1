edad = int(input("Ingrese su edad: ")) # El programa solicita al usuario que ingrese su edad y luego verifica en qué categoría se encuentra.
# Dependiendo de la edad ingresada, se imprime por pantalla la categoría correspondiente.
if edad < 12:
    print("Pertenece a la categoria de niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoria de Adolescente")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoria de adulto/a joven")
elif edad >= 30:
    print("Pertenece a la categoria de adulto/a")