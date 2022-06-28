'''
Realizar un programa que tome tres números, los ordene de mayor a menor, y
diga si el tercero es el resto de la división de los dos primeros.
'''

# Entradas
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
tercer_numero = int(input("Ingrese el tercer número: "))
numero_mayor = None
numero_menor = None
numero_de_en_medio = None
bandera_del_resto = False

# Procesos
# Subproblema 1: Determinar mayor, en medio y menor:
if primer_numero > segundo_numero and primer_numero > tercer_numero:
    numero_mayor = primer_numero
else:
    if segundo_numero > primer_numero and segundo_numero > tercer_numero:
        numero_mayor = segundo_numero
    else:
        numero_mayor = tercer_numero

if primer_numero < segundo_numero and primer_numero < tercer_numero:
    numero_menor = primer_numero
else:
    if segundo_numero < primer_numero and segundo_numero < tercer_numero:
        numero_menor = segundo_numero
    else:
        numero_menor = tercer_numero

if primer_numero != numero_mayor and primer_numero != numero_menor:
    numero_de_en_medio = primer_numero
else:
    if segundo_numero != numero_mayor and segundo_numero != numero_menor:
        numero_de_en_medio = segundo_numero
    else:
        numero_de_en_medio = tercer_numero

# Subproblema 2: Determinar si el tercero es el resto de la división del mayor y el del medio:
if numero_menor == (numero_mayor % numero_de_en_medio):
    bandera_del_resto = True

if bandera_del_resto == True:
    print("El número menor es el resto de la división del número mayor y el del medio")

# Salidas
print(numero_mayor, numero_de_en_medio, numero_menor)
