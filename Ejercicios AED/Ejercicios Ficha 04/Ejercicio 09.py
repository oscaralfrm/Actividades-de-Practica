# Simular un juego en el que se lanzan dos dados.
# Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.

import random

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Constantes
EDAD_MINIMA_CONCURSO = 18

# Entradas
edad_concursante_uno = int(input("Ingrese la edad del concursante 1: "))
edad_concursante_dos = int(input("Ingrese la edad del concursante 2: "))
edad_concursante_tres = int(input("Ingrese la edad del concursante 3: "))

# Procesos
if edad_concursante_uno >= EDAD_MINIMA_CONCURSO and edad_concursante_dos >= EDAD_MINIMA_CONCURSO and edad_concursante_tres >= EDAD_MINIMA_CONCURSO:
    print("Los 3 concursantes cumplen la edad mínima para concursar, que es de 18 años.")
else:
    print("Al menos uno de los 3 concursantes no cumple con la edad mínima para concursar.")
