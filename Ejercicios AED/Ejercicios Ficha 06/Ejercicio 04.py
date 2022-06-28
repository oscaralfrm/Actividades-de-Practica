'''
Realice un programa que permita calcular el promedio de 1000 números
aleatorios generados en el rango de [0, 100000]
'''

import random

# Datos
cont_ciclo_while = 0
acum_ciclo_while = 0

# Procesos
while cont_ciclo_while < 1000:
    numeros_aleatorios_en_rango = random.randrange(0, 100001)
    acum_ciclo_while += numeros_aleatorios_en_rango
    cont_ciclo_while += 1

else:
    promedio_azar_1000 = acum_ciclo_while // cont_ciclo_while


# Salidas
print("El promedio fue de: ", promedio_azar_1000)
