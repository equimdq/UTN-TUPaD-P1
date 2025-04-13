frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[-1]
if ultima_letra.lower() in "aeiou":
    frase += "!"

print("Resultado:", frase)
# El programa solicita al usuario que ingrese una frase o palabra y luego verifica si la última letra es una vocal.