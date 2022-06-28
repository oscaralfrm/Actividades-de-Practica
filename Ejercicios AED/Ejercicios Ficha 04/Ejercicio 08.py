# Simular un juego en el que se lanzan dos dados.
# Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.

import random

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
nombre_de_usuario = input("Ingrese su nombre: ")

# Procesos
primer_dado = random.randrange(1, 7)
segundo_dado = random.randrange(1, 7)
suma_de_dados = primer_dado + segundo_dado

print(primer_dado)
print(segundo_dado)
print(suma_de_dados)

if primer_dado == segundo_dado or (suma_de_dados % 2 == 1):
    print("¡Has ganado: ", nombre_de_usuario + "!")
else:
    print("¡Has perdido!")
