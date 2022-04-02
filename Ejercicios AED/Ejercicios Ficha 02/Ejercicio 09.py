# Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y
# determine el perímetro y la superficie del mismo.

# Menu
print("Calculador de base y altura de un rectángulo:")

# Entradas
ancho = int(input("Ingrese la cantidad de metros del ancho:"))
altura = int(input("Ingrese la cantidad de metros de la altura:"))

# Procesos
area_rectangulo = (ancho * altura)  # Devuelve una cantidad en metros cuadrados.
perimetro_rectangulo = 2* (ancho + altura)

# Salidas
print("El perímetro del rectángulo es de:",perimetro_rectangulo,"y el área es de:",area_rectangulo)
