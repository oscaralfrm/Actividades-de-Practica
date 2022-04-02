# Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:
# Valor de la hipotenusa (redondeado a 2 decimales)
# Valor del lado mayor
# Valor del lado menor


# Menu
print('*' * 50)
print("* \t\tValores Triángulo Rectángulo:\t\t\t*")
print('*' * 50)

# Entradas
cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
print('-' * 50)
cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
print('-' * 50)

# Procesos
# Valor de la Hipotenusa - usar el método round(x, 2) para redondear el valor a 2 decimales.
valor_hipotenusa = ((cateto_adyacente**2 + cateto_opuesto**2)**0.5)
hipotenusa_redondeada_a_dos_decimales = round(valor_hipotenusa, 2)


# Salidas
print("El valor de la hipotenusa de su triángulo rectángulo es de: ", hipotenusa_redondeada_a_dos_decimales)
print("El valor del cateto adyacente de su triángulo rectángulo es de: ", cateto_adyacente)
print("El valor del cateto opuesto de su triángulo rectángulo es de: ", cateto_opuesto)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. \t\t*")
print('*' * 100)
