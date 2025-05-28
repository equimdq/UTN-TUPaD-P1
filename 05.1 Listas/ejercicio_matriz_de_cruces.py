import utils
# Definicion de funciones
def imprimir_matriz_de_simbolos(nro_columnas, nro_filas, simbolo = "X"):
    for i in range(nro_filas):
        utils.imprimir_simbolos(simbolo, nro_columnas)

    

# Programa principal
ancho = utils.leer_entero_validado("Ingrese el ancho", 1)
alto = utils.leer_entero_validado("Ingrese el alto", 1)
print (f"seguimos adelante con ancho {ancho} y alto {alto}")
imprimir_matriz_de_simbolos(ancho, alto)
# Fin del programa