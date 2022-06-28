'''
Realizar un programa que tome tres números, los ordene de mayor a menor, y
diga si el tercero es el resto de la división de los dos primeros.
'''

# Entradas
primer_partido = input("Ingrese el nombre del primer partido: ")
presidente_primer_partido = input("Ingrese el nombre del/de la presidente: ")
vice_primer_partido = input("Ingrese el nombre del/de la vicepresidente: ")
votos_primer_partido = int(input("Ingrese la cantidad de votos que recibió el primer partido"))
segundo_partido = input("Ingrese el nombre del segundo partido: ")
presidente_segundo_partido = input("Ingrese el nombre del/de la presidente: ")
vice_segundo_partido = input("Ingrese el nombre del/de la vicepresidente: ")
votos_segundo_partido = int(input("Ingrese la cantidad de votos que recibió el segundo partido"))
tercer_partido = input("Ingrese el nombre del tercer partido: ")
presidente_tercer_partido = input("Ingrese el nombre del/de la presidente: ")
vice_tercer_partido = input("Ingrese el nombre del/de la vicepresidente: ")
votos_tercer_partido = int(input("Ingrese la cantidad de votos que recibió el tercer partido"))

# Procesos
formula_primer_partido = presidente_primer_partido + ' ' + vice_primer_partido
formula_segundo_partido = presidente_primer_partido + ' ' + vice_primer_partido
formula_tercer_partido = presidente_tercer_partido + ' ' + vice_tercer_partido

cantidad_total_de_votos = votos_primer_partido + votos_segundo_partido + votos_tercer_partido

porcentaje_votos_primer_partido = votos_primer_partido * 100 / cantidad_total_de_votos
porcentaje_votos_segundo_partido = votos_segundo_partido * 100 / cantidad_total_de_votos
porcentaje_votos_tercer_partido = votos_tercer_partido * 100 / cantidad_total_de_votos

# Subproblema 1: Determinar fórmula con mayor porcentaje de votos:
if porcentaje_votos_primer_partido > porcentaje_votos_segundo_partido and \
        porcentaje_votos_primer_partido > porcentaje_votos_tercer_partido:
    print("El primer partido tiene el mayor porcentaje de votos, con: ", porcentaje_votos_primer_partido)
else:


# Subproblema 2: Determinar si el tercero es el resto de la división del mayor y el del medio:

# Salidas
print(numero_mayor, numero_de_en_medio, numero_menor)
