'''
Se solicita crear un programa que permita ingresar un texto, las palabras se
encontrarán separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto. En
base a ese texto determinar:

a) La cantidad de palabras que comienzan y terminan en vocal

b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior

c) El porcentaje que representa el punto a) sobre el total de palabras del texto

'''

def validar_vocales(caracter):
    vocales = ('aeiouáéíóú')
    if caracter in vocales:
        return caracter

def programa():
    cadena = input("Ingrese una cadena de texto: ")
    cadena.lower()
    contador_de_letras = 0
    contador_palabras = 0
    contador_palabras_ct_vocal = 0
    bandera_comienza_con_vocal = False
    bandera_termina_con_vocal = False
    bandera_ct_con_vocal = False
    ultimo_caracter_palabra = car_ant = ' '


    for car in cadena:
        # AFUERA/AL FINAL DE LA PALABRA. (Acá se contabilizan las palabras).
        if car == " " or car == ".":
            if contador_de_letras > 1:
                contador_palabras += 1
                ultimo_caracter_palabra = car_ant



                # Subproblema 1
                if bandera_ct_con_vocal == True:
                    contador_palabras_ct_vocal += 1

                # Subproblema 2


                # Subproblema 3


            # Sector Reinicio
            bandera_comienza_con_vocal = False
            bandera_termina_con_vocal = False


        # DENTRO DE LA PALABRA (Acá se prenden las banderas).
        else:
            contador_de_letras += 1

            if validar_vocales(car) and contador_de_letras == 1:
                bandera_comienza_con_vocal = True

            if ultimo_caracter_palabra == caracter:
                contador_palabras_ct_vocal += 1
                ultimo_caracter_palabra = ' '


            # Subproblema 2

            car_ant = car


    # Resultados
    print("La cantidad de palabras que comienzan y terminan en la misma vocal es: ",
          contador_de_palabras_que_comienzan_y_terminan_en_vocal)




if __name__ == "__main__":
    programa()
