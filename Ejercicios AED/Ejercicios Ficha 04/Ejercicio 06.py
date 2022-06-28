# Se pide un programa que le solicite al usuario que ingrese una palabra.
# Con esa palabra calcular los siguientes puntos:
# Determinar la cantidad de letras que tiene la palabra.
# Mostrar un mensaje que informe si la palabra termina en vocal.

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
palabra_a_ingresar = input("Ingrese su palabra: ")

# Procesos
cantidad_de_letras = len(palabra_a_ingresar)
vocales = ('a', 'e', 'i', 'o', 'u')

if palabra_a_ingresar[-1] in vocales:
    print("La última letra fue una vocal.")

# Salida
print(palabra_a_ingresar)
print(cantidad_de_letras)
