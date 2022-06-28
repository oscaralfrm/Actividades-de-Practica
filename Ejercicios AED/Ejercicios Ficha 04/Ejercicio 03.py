# Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar
# el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario
# trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
# La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el
# turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora,
# si lo hace en el turno diurno cobra 35.50 pesos la hora.

'''
# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)
'''

# Constantes
PAGA_TURNO_DIURNO = 35.50
PAGA_TURNO_NOCTURNO = 40.60

# Entradas
turno_operario = int(input("Ingrese 1 para TURNO DIURNO, 2 para TURNO NOCTURNO y 3 para SALIR: "))
pago_del_empleado = 0

# Procesos
if turno_operario == 1:
    cantidad_horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    print("Usted es un EMPLEADO del TURNO DIURNO.")
    pago_del_empleado = (PAGA_TURNO_DIURNO * cantidad_horas_trabajadas)
    print("Su sueldo a ganar es de: ", pago_del_empleado, "pesos.")
else:
    if turno_operario == 2:
        cantidad_horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        print("Usted es un EMPLEADO del TURNO NOCTURNO.")
        pago_del_empleado = (PAGA_TURNO_NOCTURNO * cantidad_horas_trabajadas)
        print("Su sueldo a ganar es de: ", pago_del_empleado, "pesos.")
    else:
        if turno_operario == 3:
            print("Usted salió del sistema.")
        else:
            print("Usted NO seleccionó ninguna de las 3 opciones indicadas. Vuelva a intentarlo.")



