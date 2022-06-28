'''

Se solicita crear un programa que permita ingresar un texto, las palabras se encontraran
separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto.
En base a ese texto determinar:

a) Cantidad de palabras que comienzan con consonantes y terminan en vocales

b) Cantidad de palabras que poseen la secuencia ‘li’ a partir de la tercera letra de la palabra

c) Cantidad de palabras con menos de 4 letras y porcentaje que dicha cantidad representa sobre el total del texto

'''


'''def validar_consonantes(car):
    vocales = ("aeiouáéíóú")
    if car not in vocales:
        return car

def validar_vocales(car):
    vocales = ("aeiouáéíóú")
    if car in vocales:
        return car
'''
def programa():
    cadena = input("Ingrese una palabra: ")
    vocales = ("aeiouáéíóú")
    cadena.lower()
    contador_letras = 0
    contador_palabras = 0

    # Subproblema 1
    contador_palabras_comienzan_con_consonantes_y_terminan_en_vocales = 0
    bandera_comienza_con_consonantes = False
    bandera_termina_con_vocales = False
    car_ant = " "

    # Subproblema 2
    contador_palabras_li = 0
    bandera_l = False
    bandera_li = False

    # Subproblema 3
    contador_palabras_menos_de_4_letras = 0
    bandera_4 = False

    for car in cadena:
        # AFUERA/AL FINAL DE LA PALABRA.
        if car == " " or car == ".":
            if contador_letras > 1:
                # SIEMPRE INDENTAR TODO 1 NIVEL MÁS PROFUNDO, DENTRO DEL IF... SINO, NO CUENTA LA PALABRA.

                contador_palabras += 1

                # Subproblema 1
                if bandera_termina_con_vocales is True and bandera_comienza_con_consonantes is True:
                    contador_palabras_comienzan_con_consonantes_y_terminan_en_vocales += 1

                # Subproblema 2
                if bandera_li == True:
                    contador_palabras_li += 1

                # Subproblema 3
                if contador_letras < 4:
                    contador_palabras_menos_de_4_letras += 1



                # SECTOR REINICIO.
                bandera_comienza_con_consonantes = False
                bandera_termina_con_vocales = False
                bandera_l = False
                bandera_li = False
                bandera_4 = False


        # ADENTRO DE LA PALABRA.
        else:
            contador_letras += 1

            # Subproblema 1

            if contador_letras == 1 and car not in vocales:
                bandera_comienza_con_consonantes = True

            if car_ant in vocales:
                bandera_termina_con_vocales = True

            car_ant = car

            # Subproblema 2

            if contador_letras >= 3:
                if car == "l":
                    bandera_l = True
                if bandera_l == True and car == 'i':
                    bandera_li = True

            # Subproblema 3 - SE RESUELVE EN EL SECTOR DE PALABRAS.



    # Resultados

    # Subproblema 1
    print("La cantidad de palabras que comienzan en consonantes y terminan en vocales es: ",
          contador_palabras_comienzan_con_consonantes_y_terminan_en_vocales)

    # Subproblema 2
    print("Cantidad de palabras con \'li\' a partir de la tercera letra: ", contador_palabras_li)

    # Subproblema 3
    porcentaje_menos_de_4 = contador_palabras_menos_de_4_letras * 100 / contador_palabras
    print("La cantidad de palabras con menos de 4 letras es de: ", contador_palabras_menos_de_4_letras)
    print("El porcentaje que representan las palabras con menos de 4 letras es de: ", porcentaje_menos_de_4)


programa()
