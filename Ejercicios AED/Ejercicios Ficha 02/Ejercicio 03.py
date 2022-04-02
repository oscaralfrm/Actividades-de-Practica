# La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
# E = mc2
# Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
# Desarrolle un programa que lea el valor una masa m en kilogramos y obtenga
# la cantidad de energía E producida en la conversión.

# Menu
print("Cálculo de la ecuación de Einstein: ")

# Constantes
CONSTANTE_VELOCIDAD_DE_LA_LUZ = 299792.458

# Entradas
valor_de_la_masa = float(input("Ingrese el valor de la masa:"))

# Procesos
ecuacion_einstein_energia = valor_de_la_masa * CONSTANTE_VELOCIDAD_DE_LA_LUZ**2


# Salidas
print("La cantidad de energía producida es de: ", ecuacion_einstein_energia, "Joules.")
