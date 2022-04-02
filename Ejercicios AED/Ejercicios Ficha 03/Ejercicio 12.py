


# Menu
print('*' * 50)
print("* \t\t\t\tConteo de Votos: \t\t\t\t*")
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
