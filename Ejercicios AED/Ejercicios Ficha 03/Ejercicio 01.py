# Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo
# fijo por un cliente de un banco y calcular el saldo que tendrá esa cuenta al vencer el plazo
# fijo, sabiendo que el interés pactado era de 2.3% y que el banco cobra una tasa fija de gastos
# por servicios financieros igual $20 por cuenta.

# Menu
print('*' * 50)
print("* \tCalculadora de Intereses - Plazo Fijo: *")
print('*' * 50)

# Constantes
INTERES_PACTADO = 0.023
GASTOS_POR_SERVICIO = 20

# Entradas
dinero_depositado_a_plazo_fijo = float(input("Ingrese la cantidad de dinero a depositar a plazo fijo: "))
print('-' * 50)

# Procesos
ganancia_neta_plazo_fijo = dinero_depositado_a_plazo_fijo * INTERES_PACTADO
plazo_fijo_a_30_dias = (dinero_depositado_a_plazo_fijo + ganancia_neta_plazo_fijo) - GASTOS_POR_SERVICIO

# Salidas
print("Su dinero depositado fue de:", dinero_depositado_a_plazo_fijo, "pesos.")
print('-' * 100)
print("El interés generado por el banco cada mes con su dinero es de:", ganancia_neta_plazo_fijo, "pesos al mes.")
print('-' * 100)
print("El saldo nuevo de la cuenta será de:", plazo_fijo_a_30_dias, "pesos.")
print('-' * 100)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
