# Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
# que representaria la tarjeta de bingo de una persona. Una vez generados los números aleatorios
# solicitar al usuario que ingrese 3 números enteros y a partir de alli mostrar los siguientes mensajes:
# Si el usuario no marcó ninguno de los números indicarlo diciendo El jugador tiene mala suerte,
# no marcó ninguna casilla
# Caso contrario mostrar: El jugador marcó algún número de la tarjeta

import random


'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Datos
bandera_si_jugo_el_jugador = False
bandera_si_el_jugador_acerto = False

# Procesos
generar_numero_al_azar = 0
print("Los números de la suerte son: ")
contador_suerte = 0

# Números del jugador
primer_numero_jugador = int(input("Ingrese su primer número: "))
segundo_numero_jugador = int(input("Ingrese su segundo número: "))
tercer_numero_jugador = int(input("Ingrese su tercer número: "))
bandera_si_jugo_el_jugador = True

while contador_suerte < 15:
    if bandera_si_jugo_el_jugador == True:
        numeros_del_bingo = random.randrange(1, 101)
        print(numeros_del_bingo)
        contador_suerte += 1

# Salidas
if primer_numero_jugador == numeros_del_bingo or segundo_numero_jugador == numeros_del_bingo or tercer_numero_jugador == numeros_del_bingo:
    bandera_si_el_jugador_acerto = True
    print("El jugador marcó algún número de la tarjeta")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")






