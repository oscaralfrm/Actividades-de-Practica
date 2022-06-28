'''
Se pide desarrollar un programa en Python que permita cargar
por teclado un texto completo en una variable de tipo cadena de caracteres. Se supone que el
usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está
separada de las demás por un espacio en blanco. El programa debe:


a) Determinar cuántas palabras tienen 3, 5 o 7 letras.

b) Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera letra.

c) Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto.

d) Determinar la cantidad de palabras que contienen más de una vez la sílaba "pe".

'''

# Ya funciona.


def validar_vocales(cadena):
    vocales = ('aeiouáéíóú')
    if cadena in vocales:
        return cadena


def programa():
    cadena = input("Ingrese una cadena de texto a procesar: ")
    cadena.lower()
    contador_3_letras = 0
    contador_5_letras = 0
    contador_7_letras = 0
    contador_mas_de_3_con_vocal_en_tercera = 0
    contador_vocales = 0
    contador_palabras_con_1_o_2_vocales = 0
    contador_palabra = 0
    contador_letra = 0
    contador_palabras_con_pe = 0
    bandera_vocal_3 = False
    bandera_vocal_3_y_mayor_que_3_letras = False
    bandera_p = False
    bandera_pe = False
    bandera_1_o_2_vocales = False



    for car in cadena:
        # Estamos AFUERA o AL FINAL de cada palabra.
        if car == " " or car == ".":
            if contador_letra > 1:
                contador_palabra += 1

                # Continuación Suproblema 1

                if contador_letra == 3:
                    contador_3_letras += 1
                if contador_letra == 5:
                    contador_5_letras += 1
                if contador_letra == 7:
                    contador_7_letras += 1


                # Continuación Suproblema 2
                if bandera_vocal_3_y_mayor_que_3_letras == True:
                    contador_mas_de_3_con_vocal_en_tercera += 1


                # Continuación Subproblema 3
                if bandera_1_o_2_vocales == True:
                    contador_palabras_con_1_o_2_vocales += 1


                # Continuación Subproblema 4
                if bandera_pe == True:
                    contador_palabras_con_pe += 1



                # Sector Reinicio de variables, banderas y demás.
                # contador_palabra no se puede reinicializar, es parte de las soluciones.
                contador_letra = 0
                bandera_p = False
                bandera_pe = False
                bandera_vocal_3 = False
                bandera_vocal_3_y_mayor_que_3_letras = False
                bandera_1_o_2_vocales = False



        # Estamos DENTRO de la palabra.
        else:
            contador_letra += 1

            # Subproblema 2:

            if (validar_vocales(car)) and contador_letra == 3:
                bandera_vocal_3 = True

            # Éste if plantea, si hay una palabra con más de 3 letras y que tienen vocal en la tercera:
            if contador_letra > 3 and bandera_vocal_3:
                bandera_vocal_3_y_mayor_que_3_letras = True
                bandera_vocal_3 = False


            # Subproblema 3, promedio de palabras con 1 o 2 vocales:


            if validar_vocales(car):
                contador_vocales += 1

            if contador_vocales == 1 or contador_vocales == 2:
                bandera_1_o_2_vocales = True


            # Subproblema 4:


            if car == "p":
                bandera_p = True
            if bandera_p == True and car == "e":
                bandera_pe = True
            elif car != "p" or car != "e":
                bandera_pe = False




    # Resultados
    # Subproblema 1
    print("La cantidad de palabras con 3 letras es de: ", contador_3_letras)
    print("La cantidad de palabras con 5 letras es de: ", contador_5_letras)
    print("La cantidad de palabras con 7 letras es de: ", contador_7_letras)


    # Subproblema 2
    print("La cantidad de palabras que tienen más de 3 letras y una vocal en la tercera, es de: ",
          contador_mas_de_3_con_vocal_en_tercera)

    # Subproblema 3
    porcentaje_1_o_2_vocales = contador_palabras_con_1_o_2_vocales * 100 / contador_palabra
    print("El porcentaje total de palabras con 1 o 2 vocales sobre el resto es de: ", porcentaje_1_o_2_vocales)

    # Subproblema 4
    print("La cantidad de palabras que tienen más de una vez la sílaba \'pe\' es de: ", contador_palabras_con_pe)




if __name__ == "__main__":
    programa()
