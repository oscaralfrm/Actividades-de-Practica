# Leer dos números y calcular:
# La suma de sus cuadrados.
# El promedio de sus cubos.

# Menu
print("Calculando tanto el binomio cuadrado como el promedio de los cubos")

# Entradas

a = int(input("Primer número:"))
b = int(input("Segundo número"))

# Procesos
# Calculando la suma de sus cuadrados.
primer_elemento_al_cuadrado = int(a**2)
segundo_elemento_al_cuadrado = int(b**2)
suma_de_cuadrados = primer_elemento_al_cuadrado + segundo_elemento_al_cuadrado

# Calculando el promedio de sus cubos.
primer_elemento_al_cubo = int(a**3)
segundo_elemento_al_cubo = int(b**3)
promedio_de_cubos = (primer_elemento_al_cubo + segundo_elemento_al_cubo) // 2

# Salidas
print("La suma de cuadrados da como resultado: ", suma_de_cuadrados)
print("El promedio de los cubos da como resultado: ", promedio_de_cubos)
