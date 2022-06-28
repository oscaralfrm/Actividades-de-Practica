'''
Realizar un programa que genere 5000 numeros aleatorios en el rango de [0, 100000] y que permita:
Determinar el menor de los numeros generados en forma aleatoria
Calcular el valor promedio de los números menores a 10.000.
'''

import random

# Datos
cont_ciclo_while = 0
cont_numeros_menores_a_10000 = 0
acumulador_menores_a_10000 = 0
menor = None

# Procesos
while cont_ciclo_while < 5000:
    numeros_aleatorios_en_rango = random.randint(0, 100000)
    if menor is None:
        menor = numeros_aleatorios_en_rango
    else:
        if numeros_aleatorios_en_rango < menor:
            menor = numeros_aleatorios_en_rango
        else:
            if numeros_aleatorios_en_rango < 10000:
                acumulador_menores_a_10000 += numeros_aleatorios_en_rango
                cont_numeros_menores_a_10000 += 1
    cont_ciclo_while += 1

if cont_numeros_menores_a_10000 != 0:
    promedio = acumulador_menores_a_10000 / cont_numeros_menores_a_10000
else:
    promedio = 0

# Salidas
print("El número menor fue de: ", menor)
print("La cantidad de números menores a 10000 fue de: ", cont_numeros_menores_a_10000, "y el promedio de: ", \
      round(promedio))
