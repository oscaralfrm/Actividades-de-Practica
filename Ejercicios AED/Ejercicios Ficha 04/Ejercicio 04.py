# Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a
# diferentes momentos de un día y determinar:
# Cual es el promedio de las temperaturas.
# Si existe alguna temperatura que sea mayor al promedio.

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
temperatura_uno = float(input("Ingrese su primera medición de temperatura: "))
temperatura_dos = float(input("Ingrese su segunda medición de temperatura: "))
temperatura_tres = float(input("Ingrese su tercera medición de temperatura: "))

# Procesos
promedio_de_temperaturas = (temperatura_uno + temperatura_dos + temperatura_tres) / 3

if temperatura_uno > promedio_de_temperaturas:
    print("La primera medición de temperatura fue mayor que el promedio.")
else:
    if temperatura_dos > promedio_de_temperaturas:
        print("La segunda medición de temperatura fue mayor que el promedio.")
    else:
        if temperatura_tres:
            print("La tercera medición de temperatura fue mayor que el promedio.")

# Salidas
print("La temperatura promedio fue de: " , promedio_de_temperaturas)



