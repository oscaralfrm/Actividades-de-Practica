# Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela.
# Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rendimiento
# sabiendo que en 10 metros cuadrados se obtienen 2 quintales.

# Menu
print("Calculador de rendimiento: ")

# Entradas
largo = int(input("Ingrese la cantidad de metros de largo:"))
ancho = int(input("Ingrese la cantidad de metros de ancho:"))

# Procesos
'''
Hay que pensarlo como una regla de 3.
10 metros cuadrados - 2 quintales.
producto parcela (metros cuadrados) - X quintales.
X Quintales = (2 * producto parcela) // 10
'''
producto_parcela = (largo * ancho)  # Devuelve una cantidad en metros cuadrados.
quintales_por_parcela = (2 * producto_parcela) // 10

# Salidas
print("La cantidad de quintales de trigo es de: ", quintales_por_parcela)


