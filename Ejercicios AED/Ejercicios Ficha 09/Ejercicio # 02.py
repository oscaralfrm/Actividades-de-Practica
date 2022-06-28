'''
Desarrollar un programa en Python que permita cargar por teclado un texto.
Siempre se supone que usuario cargará un punto para indicar el final del texto, y que cada palabra de ese
texto está separada de las demás por un espacio en blanco. El programa debe determinar:

a) La cantidad de palabras que comienzan con la expresión "pa" y termina con la letra "n"

c) La cantidad de palabras que presentan mas de dos vocales a partir de la tercera letra de la palabra

d) El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad de total de palabras del texto

e) Cantidad de palabras de mas de 5 letras
'''

def es_vocal(letra):
    vocales = 'aeiouáéíóú'
    return letra in vocales

def programa():
    cant_palabras_comienzan_pa_termina_n = 0
    bandera_p = False
    bandera_pa = False
    bandera_n = False
    anterior = None
    cant_palabras_mas_de_dos_vocales_apt3lt = 0
    cant_palabras_mas_de_5_letras = 0
    palabras = 0
    letras = 0
    vocal = 0
    cadena = input("Ingrese una palabra a analizar: ")

    for car in cadena:
        if car == ' ' or car == '.':
            if letras > 0:
                palabras += 1
                if bandera_pa and bandera_n:
                    cant_palabras_comienzan_pa_termina_n += 1

                if vocal > 2:
                    cant_palabras_mas_de_dos_vocales_apt3lt += 1

                if letras > 5:
                    cant_palabras_mas_de_5_letras += 1


            # Sector Reinicio
            bandera_p = False
            bandera_pa = False
            vocal = 0
            letras = 0


        else:
            letras += 1

            if letras == 1 and car == 'p':
                bandera_p = True
            else:
                if bandera_p == True and car == 'a':
                    bandera_pa = True
                bandera_p = False


            if letras > 3:
                if es_vocal(car):
                    vocal += 1

            bandera_n = False
            if car == 'n':
                bandera_n = True


    porcentaje = cant_palabras_mas_de_dos_vocales_apt3lt * 100 / palabras

    # Resultados
    print("La cantidad de palabras que empiezan con \'pa\' y terminan en \'n\' es de: ", \
          cant_palabras_comienzan_pa_termina_n)
    print("La cantidad de palabras que presentan más de dos vocales a partir de la tercera es: ", \
          cant_palabras_mas_de_dos_vocales_apt3lt)
    print("El promedio de palabras que tienen más de 2 vocales a partir de la 3ra sobre el total es: ", \
          porcentaje)
    print("La cantidad de palabras que presentan más de 5 letras es de: ", cant_palabras_mas_de_5_letras)

if __name__ == "__main__":
    programa()
