magnitud = float(input("Ingrese la magnitud del terremoto: ")) 

# Dependiendo de la magnitud ingresada, se imprime por pantalla la categoría correspondiente.
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
# El programa solicita al usuario que ingrese la magnitud de un terremoto y luego verifica en qué categoría se encuentra.