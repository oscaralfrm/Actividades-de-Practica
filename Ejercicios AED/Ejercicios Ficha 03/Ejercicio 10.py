# Un triatlón es una competición deportiva en que los participantes realizan tres carreras:
# una de natación, una ciclista y una pedestre.
# Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) logrados en cada
# etapa por uno de los deportistas participantes.
# Con esos datos determinar:
# Tiempo total de la prueba (en formato hh:mm:ss)
# Tiempo máximo y mínimo (en segundos)
# Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
# Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones

# Menu
print('*' * 50)
print("* \t\t\t\tTiempos de Triatlón: \t\t\t\t*")
print('*' * 50)

# Entradas
nombre_candidato = (input("Ingrese el nombre del candidato: "))
print('-' * 50)
apellido_candidato = (input("Ingrese su apellido: "))
print('-' * 50)
cantidad_de_votos = int(input("Ingrese la cantidad de votos: "))
print('-' * 50)

# Procesos
# Duración del vuelo en minutos.
iniciales_del_candidato = nombre_candidato[0] + apellido_candidato[0]
cantidad_de_x_por_votos = cantidad_de_votos * 'X'


# Salidas
print("Las iniciales del candidato son: ", iniciales_del_candidato)
print("La cantidad de votos obtenidas por el candidato son: (", cantidad_de_votos, ").")
print(cantidad_de_x_por_votos)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
