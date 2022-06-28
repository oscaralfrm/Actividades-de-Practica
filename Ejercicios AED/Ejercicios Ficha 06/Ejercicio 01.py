'''
Desarrollar un programa que permita procesar funciones de un complejo de cines.
Por cada función se conoce: cantidad de espectadores y descuento (S/N).
La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).
El programa deberá:
a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50
en los días con descuento y $75 en los días sin descuento.
b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje
representan sobre el total de funciones.
'''

# Entradas
cant_espectadores = int(input("Ingrese la cantidad de espectadores en el cine: "))
valor_entrada_descuento = 50
valor_entrada_sin_descuento = 75
cont_entradas_vendidas_con_descuento = 0
acumulador_con_descuento = 0
cont_entradas_vendidas_sin_descuento = 0
acumulador_sin_descuento = 0

# Procesos
while cant_espectadores > 0:
    opcion_descuento = int(input("1. CON DESCUENTO 2. SIN DESCUENTO. 3. SALIR DEL SISTEMA.: "))
    if opcion_descuento == 1:
        cont_entradas_vendidas_con_descuento += 1
        acumulador_con_descuento += valor_entrada_descuento
        print("Hasta ahora, se han vendido: ", cont_entradas_vendidas_con_descuento, "con descuento.")
        print("Monto total acumulado por ahora: ", acumulador_con_descuento)
    else:
        if opcion_descuento == 2:
            cont_entradas_vendidas_sin_descuento += 1
            acumulador_sin_descuento += valor_entrada_sin_descuento
            print("Hasta ahora, se han vendido: ", cont_entradas_vendidas_sin_descuento, "con descuento.")
            print("Monto total acumulado por ahora: ", acumulador_sin_descuento)
        else:
            if opcion_descuento == 3:
                print("¡Gracias por usar nuestro sistema!")
                cant_espectadores -= cant_espectadores
    cant_espectadores -= 1

recaudacion_total_con_descuento = valor_entrada_descuento * cont_entradas_vendidas_con_descuento
recaudacion_total_sin_descuento = valor_entrada_sin_descuento * cont_entradas_vendidas_sin_descuento
recaudacion_definitiva = recaudacion_total_con_descuento + recaudacion_total_sin_descuento
cantidad_total_vendidas = cont_entradas_vendidas_con_descuento + cont_entradas_vendidas_sin_descuento
porcentaje_descuento_vendidos = cont_entradas_vendidas_con_descuento * 100 / cantidad_total_vendidas



# Salidas
print("La recaudación definitiva fue de: ", recaudacion_definitiva, "pesos.")
print("Las entradas con descuento supusieron un porcentaje de ventas del total de: ", \
      round(porcentaje_descuento_vendidos, 0), "%.")
