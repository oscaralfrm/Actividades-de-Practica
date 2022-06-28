# Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
# Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:
# Verificar si todos los cuadros son anteriores al siglo XX
# (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
# Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
# Informar la diferencia en años entre la obra más nueva y la más antigua.

import random

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Constantes
INICIO_SIGLO_XX = 1901
FIN_SIGLO_XX = 2000

# Entradas
nombre_del_primer_cuadro = input("Ingrese el nombre del primer cuadro: ")
año_creacion_primer_cuadro = int(input("Ingrese el año de creación del primer cuadro: "))
nombre_del_segundo_cuadro = input("Ingrese el nombre del segundo cuadro: ")
año_creacion_segundo_cuadro = int(input("Ingrese el año de creación del segundo cuadro: "))
nombre_del_tercer_cuadro = input("Ingrese el nombre del tercer cuadro: ")
año_creacion_tercer_cuadro = int(input("Ingrese el año de creación del tercer cuadro: "))
usuario_ingresa_algun_anio = int(input("Ingrese algún año:"))

# Procesos
obra_mas_nueva = None
obra_mas_antigua = None

if año_creacion_primer_cuadro >= INICIO_SIGLO_XX and año_creacion_primer_cuadro <= FIN_SIGLO_XX and año_creacion_segundo_cuadro >= INICIO_SIGLO_XX and año_creacion_segundo_cuadro <= FIN_SIGLO_XX and año_creacion_tercer_cuadro >= INICIO_SIGLO_XX and año_creacion_tercer_cuadro <= FIN_SIGLO_XX:
    print("Todos los años pertecene al Siglo XX.")


if año_creacion_primer_cuadro > año_creacion_segundo_cuadro and año_creacion_primer_cuadro > año_creacion_segundo_cuadro:
    obra_mas_nueva = año_creacion_primer_cuadro
else:
    if año_creacion_segundo_cuadro > año_creacion_primer_cuadro and año_creacion_segundo_cuadro > año_creacion_primer_cuadro:
        obra_mas_nueva = año_creacion_segundo_cuadro
    else:
        if año_creacion_tercer_cuadro > año_creacion_primer_cuadro and año_creacion_tercer_cuadro > año_creacion_primer_cuadro:
            obra_mas_nueva = año_creacion_tercer_cuadro

if año_creacion_primer_cuadro < año_creacion_segundo_cuadro and año_creacion_primer_cuadro < año_creacion_segundo_cuadro:
    obra_mas_antigua = año_creacion_primer_cuadro
else:
    if año_creacion_segundo_cuadro < año_creacion_primer_cuadro and año_creacion_segundo_cuadro < año_creacion_primer_cuadro:
        obra_mas_antigua = año_creacion_segundo_cuadro
    else:
        if año_creacion_tercer_cuadro < año_creacion_primer_cuadro and año_creacion_tercer_cuadro < año_creacion_primer_cuadro:
            obra_mas_antigua = año_creacion_tercer_cuadro

diferencia_obra_nueva_y_vieja = obra_mas_nueva - obra_mas_antigua

if usuario_ingresa_algun_anio == año_creacion_primer_cuadro:
    print("La primera obra coincide con el año que ingresó.")
else:
    if usuario_ingresa_algun_anio == año_creacion_segundo_cuadro:
        print("La segunda obra coincide con el año que ingresó.")
    else:
        if usuario_ingresa_algun_anio == año_creacion_tercer_cuadro:
            print("La tercera obra coincide con el año que ingresó.")

# Salidas
