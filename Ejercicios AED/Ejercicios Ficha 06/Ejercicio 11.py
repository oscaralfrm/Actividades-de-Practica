'''
Un matemático desea un simple programa que le permita cargar
una serie de números que representan los discriminantes de diferentes ecuaciones de segundo grado,
el proceso de la secuencia finaliza cuando el matemático no desea seguir cargando discriminantes. Usted debe:
a) Determinar la cantidad de discriminantes que darán 2 raíces
b) Determinar la cantidad de discriminantes que darán una única raíz
c) Determinar la cantidad de discriminantes que daran raíces en el campo de los números imaginarios
d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático
'''

import random

# Datos

categoria_de_venta = int(input("Ingrese el número de la categoría de venta. 0 para SALIR: "))
acum_categoria_1 = 0
acum_categoria_2 = 0
acum_categoria_3 = 0
acum_categoria_4 = 0
comision_categoria_1 = 0
comision_categoria_2 = 0
comision_categoria_3 = 0
comision_categoria_4 = 0

# Procesos

while categoria_de_venta != 0:
    total_venta = float(input("Ingrese la cantidad de dinero total por concepto de venta: "))
    if categoria_de_venta == 1:
        comision_categoria_1 = total_venta * 10 / 100
        acum_categoria_1 += comision_categoria_1
    if categoria_de_venta == 2:
        comision_categoria_2 = total_venta * 20 / 100
        acum_categoria_2 += comision_categoria_2
    if categoria_de_venta == 3:
        comision_categoria_3 = total_venta * 30 / 100
        acum_categoria_3 += comision_categoria_3
    if categoria_de_venta == 4:
        comision_categoria_4 = total_venta * 40 / 100
        acum_categoria_4 += comision_categoria_4
    categoria_de_venta = int(input("Ingrese de nuevo la categoría. 0 para SALIR."))

total_de_acum = acum_categoria_1 + acum_categoria_2 + acum_categoria_3 +acum_categoria_4

# Salidas
print("La cantidad total de comisiones de la categoría 1 es de: ", comision_categoria_1)
print("La cantidad total de comisiones de la categoría 2 es de: ", comision_categoria_2)
print("La cantidad total de comisiones de la categoría 3 es de: ", comision_categoria_3)
print("La cantidad total de comisiones de la categoría 4 es de: ", comision_categoria_4)
print("La cantidad total comisiones de todas las categorías es de: ", total_de_acum)
