# Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva
# enmascarada, mostrando la primer letra y la última, pero reemplazando los caracteres intermedios
# por asteriscos.
# Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.

# Menu
print('*' * 50)
print("* \t\t\t\tPalabra Enmascarada: \t\t\t*")
print('*' * 50)

# Entradas
palabra_que_sera_enmascarada = input("Ingrese su palabra a enmascarar: ")  # El resultado será un string.

# Procesos
cantidad_de_letras_enmascaradas = len(palabra_que_sera_enmascarada) - len(palabra_que_sera_enmascarada[0]) - len(palabra_que_sera_enmascarada[-1])
asterisco_por_enmascaramiento = ('*' * cantidad_de_letras_enmascaradas)
palabra_enmascarada_final = (palabra_que_sera_enmascarada[0] + asterisco_por_enmascaramiento + palabra_que_sera_enmascarada[-1])

# Salidas
print("Su palabra final a enmascarar es: ", palabra_enmascarada_final)
print('*' * 100)
print("* \t\tGracias por usar nuestro servicio, que pase un excelente día. Fin del programa. *")
print('*' * 100)
