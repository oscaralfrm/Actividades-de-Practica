'''
* Ejercicio tipo Parcial*
Para calcular el premio de un vendedor, se ingresan
3 montos correspondientes a sus ventas mensuales del último trimestre.
El premio es equivalente al 50% del menor monto vendido. Si además todos los montos superan los $1000,
se agrega un 10% adicional al premio calculado.
'''

# Entradas
primer_mes = int(input("Ingrese el monto correspondiente al primer mes: "))
segundo_mes = int(input("Ingrese el monto correspondiente al segundo mes: "))
tercer_mes = int(input("Ingrese el monto correspondiente al tercer mes: "))

suma_de_todos_los_meses = primer_mes + segundo_mes + tercer_mes
menor_monto = 0

# Procesos
if primer_mes < segundo_mes and primer_mes < tercer_mes:
    menor_monto = primer_mes
    print("El mes con el menor monto de venta fue el primero, con un monto de: ", menor_monto, "pesos.")
else:
    if segundo_mes < primer_mes and segundo_mes < tercer_mes:
        menor_monto = segundo_mes
        print("El mes con el menor monto de venta fue el segundo, con un monto de: ", menor_monto, "pesos.")
    else:
        menor_monto = tercer_mes
        print("El mes con el menor monto de venta fue el tercero, con un monto de: ", menor_monto, "pesos.")

if suma_de_todos_los_meses > 1000:
    premio_por_ventas = menor_monto * 60 / 100
    print("¡Enhorabuena! El premio por ventas aumentó y ahora es de: ", premio_por_ventas, "pesos.")
else:
    if suma_de_todos_los_meses < 1000:
        premio_por_ventas = menor_monto * 50 / 100
        print("El premio por sus ventas fue de: ", premio_por_ventas, "pesos.")

