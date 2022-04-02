# Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional
# al cual pertenece. Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del
# 8% sobre su salario actual y un descuento de 2.5% por servicios, informando los resultados con
# el formato que se especifica a continuación:
#       Nombre Empleado: xxxxxxxxx            Nuevo Salario: $ xxx

#       Área Funcional:  xxxxxxxxxxxx

#       Salario Actual: $ xxxx

# Constante
INCREMENTO_DEL_SALARIO = 0.08
DESCUENTO_POR_SERVICIOS = 0.025

# Menu
print('*' * 50)
print("* \t\t\t\tCalculadora de Sueldo: \t\t\t*")
print('*' * 50)

# Entradas
nombre_del_empleado = input("Ingrese su nombre y apellido: ")
print('-' * 100)
area_funcional = input("Ingrese su área funcional de trabajo: ")
print('-' * 100)
salario_actual = float(input("Ingrese su salario actual: "))
print('-' * 100)

# Procesos
salario_con_incremento = salario_actual + (salario_actual * INCREMENTO_DEL_SALARIO)
salario_reducido = salario_actual * DESCUENTO_POR_SERVICIOS
salario_total = salario_con_incremento - salario_reducido

# Salidas
print("\t\t\t\tNombre Empleado: ", nombre_del_empleado, "\t\t\t\t\t\tNuevo Salario: ", salario_total)
print("\t\t\t\tÁrea Funcional: ", area_funcional)
print("\t\t\t\tSalario Actual $: ", salario_actual)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
