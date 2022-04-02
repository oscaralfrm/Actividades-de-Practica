# Plantear un script (directamente en el shell de Python) que permita informar,
# para dos valores a y b el resultado de la división a/b y el resto de esa divisón.

# Entradas

a = int(input("Primer número:"))
b = int(input("Segundo número:"))

# Procesos
resultado_division = int(a / b)
resto_division = int(a % b)

# Salidas
print("El resultado de su división es:", resultado_division, "y el resto fue de:", resto_division)
