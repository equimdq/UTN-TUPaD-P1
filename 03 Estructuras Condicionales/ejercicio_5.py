contraseña = input ("Introduce la contraseña: ") # El programa solicita al usuario que ingrese una contraseña y luego verifica si cumple con la longitud requerida.
# Dependiendo de la longitud ingresada, se imprime por pantalla si la contraseña es correcta o no.
longitud = len(contraseña)
if 8 <= longitud <= 14:
    print ("Ha ingresado una contraseña correcta")
else: 
    print ("Por favor ingrese una contraseña de entre 8 y 14 caracteres")