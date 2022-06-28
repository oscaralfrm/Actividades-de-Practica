'''
Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus
vendedores, para ello le solicita un sistemita que le permita calcular dicho montos.
Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4).
Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta (el proceso
termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por
los vendedores de diferentes en base a los siguientes cálculos:
a) Categoría 1: cobra una comisión de 10%
b) Categoría 2: cobra una comisión de 25%
c) Categoría 3: cobra una comisión de 30%
d) Categoría 4: cobra una comisión de 40%
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de v
endedores que tiene la empresa junto con el total general
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
