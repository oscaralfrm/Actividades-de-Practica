# En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología.
# El presupuesto anual del hospital se reparte de la siguiente manera:
# Urgencias 37%
# Pediatría 42%
# Traumatología 21%
# Cargar por teclado el monto del presupuesto total del hospital, y calcular y
# mostrar el monto que recibirá cada área.

# Menu
print('*' * 50)
print("* \t\tCálculo de Presupuesto Hospitalario: \t*")
print('*' * 50)

# Constantes
PORCENTAJE_URGENCIAS = 0.37
PORCENTAJE_PEDIATRIA = 0.42
PORCENTAJE_TRAUMATOLOGIA = 0.21

# Entradas
presupuesto_hospitalario_inicial = float(input("Ingrese el presupuesto inicial por mes del Hospital: "))
print('-' * 50)

# Procesos
# Presupuesto al mes por cada área de especialización:
presupuesto_urgencias = presupuesto_hospitalario_inicial * PORCENTAJE_URGENCIAS
presupuesto_pediatria = presupuesto_hospitalario_inicial * PORCENTAJE_PEDIATRIA
presupuesto_traumatologia = presupuesto_hospitalario_inicial * PORCENTAJE_TRAUMATOLOGIA


# Salidas
print("El presupuesto por cada área de especialización es: ")
print("Urgencias: ", presupuesto_urgencias)
print("Pediatría: ", presupuesto_pediatria)
print("Traumatología: ", presupuesto_traumatologia)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
