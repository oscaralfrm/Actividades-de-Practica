# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

# yardas
# pulgadas
# centímetros
# metros
# Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.

# Menu
print("Conversor de unidades de distancia (de pies a otras)")

# Entradas
input_de_pies = float(input("Ingrese un valor de medidas de pies: "))

# Procesos
conversor_pies_a_yardas = input_de_pies / 3
conversor_pies_a_pulgadas = input_de_pies * 12
conversor_pies_a_centimetros = conversor_pies_a_pulgadas * 2.54
conversor_pies_a_metros = conversor_pies_a_centimetros / 100


# Salidas
print(input_de_pies, "a yardas son: ", conversor_pies_a_yardas, "yardas.")
print(input_de_pies, "a pulgadas son: ", conversor_pies_a_pulgadas, "pulgadas.")
print(input_de_pies, "a centímetros son: ", conversor_pies_a_centimetros, "centímetros.")
print(input_de_pies, "a metros son: ", conversor_pies_a_metros, "metros.")
