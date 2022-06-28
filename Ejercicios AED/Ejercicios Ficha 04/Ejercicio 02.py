# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es
# mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Entradas
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))
resultado_final = 0

# Procesos
suma_de_numeros = numero_uno + numero_dos + numero_tres

if suma_de_numeros > 10:
    resultado_final = suma_de_numeros // 2
else:
    resultado_final = suma_de_numeros ** 3

print("La suma de sus números dependiendo de su resultado es de: ", resultado_final)

