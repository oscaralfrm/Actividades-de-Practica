# Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo
# (hora y minutos), determine cuál es su duración en minutos. Si el viajero necesita
# luego 45 minutos más para ir del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?

# Menu
print('*' * 50)
print("* \t\t\t\tDuración de Vuelo: *")
print('*' * 50)

# Constante
MINUTOS_PARA_LLEGAR_AL_HOTEL = 45  # Cantidad de minutos que tarda en llegar el pasajero al hotel.

# Entradas
horario_de_salida_avion_horas = int(input("Ingrese la cantidad de horas de su vuelo: "))
print('-' * 50)
horario_de_salida_avion_minutos = int(input("Ingrese la cantidad de minutos de su vuelo: "))
print('-' * 50)

# Procesos
# Duración del vuelo en minutos.
conversion_horas_a_minutos = horario_de_salida_avion_horas * 60
suma_de_minutos_de_vuelo = conversion_horas_a_minutos + horario_de_salida_avion_minutos
# Llegada al hotel en horas.
llegada_al_hotel = (suma_de_minutos_de_vuelo + MINUTOS_PARA_LLEGAR_AL_HOTEL) // 60

# Salidas
print("Tiempo de Vuelo en minutos: ", suma_de_minutos_de_vuelo)
print("Horas desde el aeropuerto hacia el hotel: ", llegada_al_hotel)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
