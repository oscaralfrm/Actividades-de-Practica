'''
Realizar un programa que permita buscar el mayor de 10.000 números aleatorios
generados en el rango de [0, 100.000].
'''

import random

# Datos
cont_ciclo_while = 0
mayor_ciclo_while = 0
bandera_primera_vuelta = True

# Procesos
while cont_ciclo_while < 10000:
    numeros_aleatorios_en_rango = random.randrange(0, 100001)
    if bandera_primera_vuelta == True:
        mayor_ciclo_while = 0
        bandera_primera_vuelta = False
    else:
        if numeros_aleatorios_en_rango > mayor_ciclo_while:
            mayor_ciclo_while = numeros_aleatorios_en_rango
    cont_ciclo_while += 1

# Salidas
print("El número mayor fue de: ", mayor_ciclo_while)
