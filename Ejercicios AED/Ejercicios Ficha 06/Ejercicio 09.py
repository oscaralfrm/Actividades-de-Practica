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
numero_de_serie = int(input("Ingrese un número: "))
mayor = None
orden = 0

# Datos a CARGAR
while numero_de_serie != 0:
    if numero_de_serie % 2 == 0 and orden % 2 == 0:
        if mayor == None or numero_de_serie > mayor:
            mayor = numero_de_serie
        # Se busca el mayor
    orden += 1
    numero_de_serie = int(input("Ingrese un número: "))

print("El número mayor ingresado es de: ", mayor)


# Procesos

# Salidas
