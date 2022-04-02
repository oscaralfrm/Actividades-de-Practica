# En el Congreso se vota la sanción de una ley muy importante.
# Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra,
# e informe el porcentaje obtenido en cada caso.

# Menu
print("Cantidad de votos por partido: ")

# Entradas
votos_a_favor = int(input("Ingrese la cantidad de votos a favor:"))
votos_en_contra = int(input("Ingrese la cantidad de votos en contra:"))

# Procesos
votos_totales = votos_a_favor + votos_en_contra
porcentaje_votos_a_favor = votos_a_favor / votos_totales * 100
porcentaje_votos_en_contra = votos_en_contra / votos_totales * 100

# Salidas
print("La cantidad de votos a favor es de: ", votos_a_favor, "y su porcentaje de aprobación es de", porcentaje_votos_a_favor, "%")
print("La cantidad de votos a favor es de: ", votos_en_contra, "y su porcentaje de aprobación es de", porcentaje_votos_en_contra, "%")
