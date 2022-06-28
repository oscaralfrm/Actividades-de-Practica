'''
* Ejercicio tipo Parcial*
Para un análisis estadístico, se pide ingresar 3 valores y determinar:
Si alguno de los valores es múltiplo de 5
Cuántos de los valores son impares
Si el mayor de ellos supera a la suma de los otros 2
'''

# Entradas
valor1 = int(input("Ingrese el primer valor numérico: "))
valor2 = int(input("Ingrese el segundo valor numérico: "))
valor3 = int(input("Ingrese el tercer valor numérico: "))

bandera_multiplo_de_5 = False
cont_impares = 0
valor_mayor = 0
valor_menor_1 = 0
valor_menor_2 = 0

# Procesos
if valor1 % 5 == 0:
    bandera_multiplo_de_5 = True
    if valor1 % 2 != 0:
        cont_impares += 1
else:
    if valor2 % 5 == 0:
        bandera_multiplo_de_5 = True
        if valor2 % 2 != 0:
            cont_impares += 1
    else:
        if valor3 % 5 == 0:
            bandera_multiplo_de_5 = True
            if valor3 % 2 != 0:
                cont_impares += 1

if valor1 > valor2 and valor1 > valor3:
    valor_mayor = valor1
    valor_menor_1 = valor2
    valor_menor_2 = valor3
else:
    if valor2 > valor1 and valor2 > valor3:
        valor_mayor = valor2
        valor_menor_1 = valor1
        valor_menor_2 = valor3
    else:
        valor_mayor = valor3
        valor_menor_1 = valor1
        valor_menor_2 = valor2

if bandera_multiplo_de_5 == True:
    print("Al menos uno de los valores ingresados es múltiplo de 5.")

if valor_mayor > (valor_menor_1 + valor_menor_2):
    print("El valor mayor es superior a la suma de los otros dos.")
else:
    print("El valor mayor NO es superior a la suma de los otros dos.")

