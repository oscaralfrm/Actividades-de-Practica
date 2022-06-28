# Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:
# 1) Informar si entre las cartas se encuentra el as de espadas
# 2) Verificar si las tres cartas son del mismo palo. Si es así,
# identificar cuál fue la mayor carta. En caso contrario, informarlo.

import random

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
tupla_de_cartas = ('Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Reina (Q)', 'Rey (K)', 'Comodín (J)')
tupla_de_palos = ('de Corazones', 'de Diamantes', 'de Espadas', 'de Tréboles')
mayor_del_mismo_palo = None

# Procesos
seleccion_de_primera_carta = random.choice(tupla_de_cartas) + ' ' + random.choice(tupla_de_palos)
seleccion_de_segunda_carta = random.choice(tupla_de_cartas) + ' ' + random.choice(tupla_de_palos)
seleccion_de_tercera_carta = random.choice(tupla_de_cartas) + ' ' + random.choice(tupla_de_palos)

if (seleccion_de_primera_carta == (tupla_de_cartas[0] + ' ' + tupla_de_palos[2]) or
    seleccion_de_segunda_carta == (tupla_de_cartas[0] + ' ' + tupla_de_palos[2]) or
    seleccion_de_tercera_carta) == (tupla_de_cartas[0] + ' ' + tupla_de_palos[2]):
    print("Se encontró el Ás de Espadas en alguna de las 3 tiradas.")

if seleccion_de_primera_carta(random.choice(tupla_de_palos)) == seleccion_de_segunda_carta(random.choice(tupla_de_palos))\
        or seleccion_de_primera_carta(random.choice(tupla_de_palos)) == seleccion_de_tercera_carta(random.choice(tupla_de_palos))\
        or seleccion_de_segunda_carta(random.choice(tupla_de_palos)) == seleccion_de_tercera_carta(random.choice(tupla_de_palos)):
    print("Las 3 cartas son del mismo palo.")
    if seleccion_de_primera_carta > seleccion_de_segunda_carta and seleccion_de_primera_carta > seleccion_de_tercera_carta:
        print("La primera carta fue la mayor.")
    else:
        if seleccion_de_segunda_carta > seleccion_de_primera_carta and seleccion_de_segunda_carta > seleccion_de_tercera_carta:
            print("La segunda carta fue la mayor.")
        else:
            print("La tercera carta fue la mayor.")


# Salidas
print(seleccion_de_primera_carta)
print(seleccion_de_segunda_carta)
print(seleccion_de_tercera_carta)
