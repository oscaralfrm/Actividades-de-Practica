'''
Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al
ingresar cualquier otro valor para sexo.
El programa debe informar:
a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
c) Si hay algún varón que supere los 80 años de edad
'''

import random

# Datos a CARGAR
sexo_habitante = input("Ingrese su SEXO: M para HOMBRE/F para MUJER; otra letra para terminar: ")
cant_hombres = 0
cant_mujeres = 0
cant_mujeres_edad_escolar = 0
cant_hombres_mayores_a_80 = False

# Procesos
while sexo_habitante == 'M' or sexo_habitante == 'F':
    edad_habitante = int(input("Ingrese su EDAD: "))
    if sexo_habitante == 'M':
        cant_hombres += 1
        if sexo_habitante == 'M' and edad_habitante > 80:
            cant_hombres_mayores_a_80 = True
    if sexo_habitante == 'F':
        cant_mujeres += 1
        if sexo_habitante == 'F' and edad_habitante >= 4 and edad_habitante <= 18:
            cant_mujeres_edad_escolar += 1
    sexo_habitante = input("Ingrese su SEXO: M para HOMBRE/F para MUJER; otra letra para terminar: ")

# Salidas
if cant_hombres > cant_mujeres:
    print("La cantidad de hombres es mayor que la de mujeres.")
else:
    if cant_mujeres > cant_hombres:
        print("La cantidad de mujeres es mayor que la de hombres.")
    else:
        if cant_hombres == cant_mujeres:
            print("Hay la misma cantidad de hombres y de mujeres.")

if cant_hombres_mayores_a_80 == True:
    print("Hay al menos un hombre que supere los 80 años de edad.")

print("La cantidad de mujeres en edad escolar es de: ", cant_mujeres_edad_escolar)

