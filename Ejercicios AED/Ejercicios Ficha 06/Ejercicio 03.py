'''
Realice un programa que le ofrezca al usuario un menú de opciones
que le permita ejecutar las siguientes acciones:
Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].
Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].
Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000]
y calcular el valor promedio de los números menores a 10.000.
Cualquier otro número: Salir del programa.
'''

import random

# Entradas
op = int(input("1. PROMEDIO DE 1000 NÚMEROS. 2. MAYOR DE 10000 NÚMEROS. 3. MENOR 5000 NÚMEROS Y PROM. MENORES. "))

# Procesos
while op > 0 and op < 4:
    if op == 1:
        cont_ciclo_op_1 = 0
        acum_ciclo_op_1 = 0
        while cont_ciclo_op_1 < 1000:
            n = random.randint(0, 100000)
            acum_ciclo_op_1 += n
            cont_ciclo_op_1 += 1
        prom_1 = acum_ciclo_op_1 / cont_ciclo_op_1
        print("El promedio de 1000 números aleatorios es de: ", round(prom_1))
        op = int(input("Seleccione la misma u otra opción: "))
    if op == 2:
        mayor = 0
        cont_ciclo_op_2 = 0
        while cont_ciclo_op_2 < 10000:
            n = random.randint(1, 100000)
            if mayor < n:
                mayor = n
            cont_ciclo_op_2 += 1
        print("El mayor número de 10000 valores es de: ", mayor)
        op = int(input("Seleccione la misma u otra opción: "))
    if op == 3:
        menor = 100000
        cont_ciclo_op_3 = 0
        acum_ciclo_op_3_menores_10000 = 0
        cont_ciclo_op_3_menores_10000 = 0
        while cont_ciclo_op_3 < 5000:
            n = random.randint(1, 100000)
            if menor > n:
                menor = n
            if n < 10000:
                acum_ciclo_op_3_menores_10000 += n
                cont_ciclo_op_3_menores_10000 += 1
            cont_ciclo_op_3 += 1
        prom_3 = acum_ciclo_op_3_menores_10000 / cont_ciclo_op_3_menores_10000
        print("El número menor es: ", menor)
        print("El promedio de números menores a 10000 es de: ", round(prom_3))
        op = int(input("Seleccione la misma u otra opción: "))





