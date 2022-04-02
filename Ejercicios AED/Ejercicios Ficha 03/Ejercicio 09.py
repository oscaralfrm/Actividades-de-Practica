# Una pequeña empresa de informática tiene que desarrollar un sistema de información y
# para ello tiene un presupuesto de x pesos para cubrir los costos de crear el sistema.
# Sabiendo que tiene pensado ganar al menos 17% por el proyecto, determine cuál es el valor
# máximo que pueden alcanzar los costos del proyecto.


# Menu
print('*' * 50)
print("* \t\t\t\tCostos del Proyecto: \t\t\t*")
print('*' * 50)

# Entradas
presupuesto_costos_del_sistema = float(input("Ingrese la cantidad de presupuesto: "))
print('-' * 50)


# Procesos
# Ejercicio que se resuelve mediante regla de 3 simple:
# Input del usuario (X) pesos - 100%
# Nuevo presupuesto cortando gastos (desconocido) - 17%
# Calcularle el 17% al input del usuario, y restarlo al input del usuario.
# presupuesto_final_para_maximizar_ganancias = input del usuario - corte_de_gastos
corte_de_gastos = (presupuesto_costos_del_sistema * 0.17) / 1
presupuesto_final_para_maximizar_ganancias = presupuesto_costos_del_sistema - corte_de_gastos

# Salidas
print("Su presupuesto inicial es de: ", presupuesto_costos_del_sistema)
print("El presupuesto máximo que usted puede gastar es de: ", presupuesto_final_para_maximizar_ganancias, "para conseguir un 17% de ganancias.")
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. \t\t*")
print('*' * 100)
