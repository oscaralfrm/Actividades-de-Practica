# Un persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos mas extremos
# (Ushuahia y La Quiaca)
# en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.
# Nuestro aventurero efectivamente inició la travesía pero se accidentó y sólo recorrió x metros según su GPS.
# Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro
# aventurero y qué porcentaje represento lo recorrido del total de kms a recorrer de Ushuahia a
# La Quiaca (para el porcentaje usted deberá realizar los calculos en metros).

# Menu
print('*' * 50)
print("* \t\t\tCálculo Distancia de Viaje: \t\t*")
print('*' * 50)

# Constante
RECORRIDO_DE_PUNTO_A_PUNTO = 3641.3
RECORRIDO_EN_METROS = RECORRIDO_DE_PUNTO_A_PUNTO * 1000

# Entradas
cantidad_metros_gps = float(input("¿Cuántos metros marcó en su GPS?: "))
print('-' * 50)

# Procesos
# Duración del vuelo en minutos.
cantidad_en_kilometros_gps = cantidad_metros_gps / 1000
cantidad_recorrida_total_en_metros = RECORRIDO_EN_METROS - cantidad_metros_gps
cantidad_recorrida_total_en_kilometros = RECORRIDO_DE_PUNTO_A_PUNTO - cantidad_en_kilometros_gps
# Plantear una regla de 3 para determinar el porcentaje del total recorrido en metros.
#  RECORRIDO EN METROS (3641300 m) - 100%
#  Input del usuario en metros         - X
#  X = Input en metros * 100 / RECORRIDO EN METROS (3641300 m)
porcentaje_recorrido_en_metros = cantidad_metros_gps * 100 / RECORRIDO_EN_METROS

# Salidas
print("La cantidad total de kilómetros recorrida fue de: ", cantidad_en_kilometros_gps, "kilómetros")
print("La cantidad total de metros recorrida fue de: ", cantidad_metros_gps, "metros")
print("El porcentaje del total recorrido fue de: ", porcentaje_recorrido_en_metros, "%")
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
