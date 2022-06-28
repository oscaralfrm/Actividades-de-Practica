# Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente.
# Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.

import random

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
apuesta_del_jugador = int(input("Ingrese la cantidad de dinero a apostar: "))
seleccion_del_jugador = int(input("Seleccione 1 si apuesta por CARA, y 2 si apuesta por CRUZ: "))

# Procesos
moneda = ("cara", "cruz")

if seleccion_del_jugador == 1:
    moneda = "cara"
else:
    if seleccion_del_jugador == 2:
        moneda = "cruz"

apuesta_con_moneda = random.choice(moneda)
print(apuesta_con_moneda)

if seleccion_del_jugador == apuesta_con_moneda:
    print("Usted ganó: ", apuesta_del_jugador * 2, "pesos.")
else:
    print("Usted perdió y perdió su dinero.")
