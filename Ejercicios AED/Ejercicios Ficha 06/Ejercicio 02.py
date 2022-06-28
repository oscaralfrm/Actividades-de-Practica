'''
Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en
las diferentes sucursales de un país de una determinada empresa.
Los requerimientos funcionales del programa son:
a) Informar la cantidad de ventas ingresadas.
b) Total de ventas.
c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
d) Cantidad de ventas con 400, 500 y 600 unidades.
e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.
Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.
'''

# Entradas
cont_total_ventas = 0
cont_ventas_100_300 = 0
cont_ventas_400_500_600 = 0
acum_ventas = 0
bandera_venta_50 = False
num = 0


# Procesos
while num >= 0:
    valor_numero_ventas = int(input("Ingrese el valor de las unidades vendidas: "))
    if valor_numero_ventas >= 100 and valor_numero_ventas <= 300:
        cont_ventas_100_300 += 1
    else:
        if valor_numero_ventas == 400 or valor_numero_ventas == 500 or valor_numero_ventas == 600:
            cont_ventas_400_500_600 += 1
        else:
            if valor_numero_ventas < 50:
                bandera_venta_50 = True
    acum_ventas += valor_numero_ventas
    cont_total_ventas += 1
    num = int(input("Ingrese un 0 o un valor mayor que 0 para SEGUIR, o un negativo para SALIR."))

# Salidas

print("La unidades vendidas fue de: ", acum_ventas)
print("La cantidad total de ventas fue de: ", cont_total_ventas)
print("La cantidad de unidades vendidas entre el rango de 100 y 300 fue de: ", cont_ventas_100_300)
print("La cantidad de unidades vendidas que fueron exactamente de 400, 500 o 600 unidades fue de: ", \
      cont_ventas_400_500_600)
if bandera_venta_50 == True:
    print("Hubo una venta que facturó por menos de 50 unidades.")
