# Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone
# representa una fecha en formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año.
# Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

# Menu
print('*' * 50)
print("* \tCalendario Digital *")
print('*' * 50)

# Entradas
dia = int(input("Ingrese el día: "))
print('-' * 50)
mes = int(input("Ingrese el mes: "))
print('-' * 50)
anio = int(input("Ingrese el año: "))
print('-' * 50)

# Procesos
calendario = ("Día:", dia, "-", "Mes:", "-", mes, "Año:", anio)

# Salidas
print("La fecha en la que ustes se encuentra es: ", calendario)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
