'''
Desarrollar un programa en Python que permita cargar por teclado un texto completo.
Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de
ese texto está separada de las demás por un espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían exactamente 3 letras.

b) Determinar el porcentaje que las palabras del punto 1 representan en el total del palabras del texto.

c) Determinar cuántas palabras terminaban con la letra "s".

d) Determinar cuántas palabras contuvieron al menos una vez la expresión "dre".

'''

# Ya funciona.


def program():
    cadena = input("Ingrese una cadena: ")
    cadena.lower()
    contador_letras = 0
    contador_palabras = 0

    # Subproblema 1 - RESOLVER CON BANDERAS Y FUERA DE LA PALABRA.
    contador_palabras_3_letras = 0

    # Subproblema 2 - RESOLVER EN EL APARTADO DE RESULTADOS CON CÁLCULO DE PORCENTAJES.

    # Subproblema 3 - UTILIZAR EL ULTIMO CARACTER, TOMAR EL VALOR DE CAR Y COMPARAR SI ES LA LETRA S.
    ultimo_caracter = " "
    bandera_palabras_que_terminan_en_s = False
    contador_palabras_que_terminan_en_s = 0

    # Subproblema 4 - USAR 3 BANDERAS, PARA LA D, PARA LA DR, Y POR ULTIMO DRE. RESOLVER FUERA DE LA PALABRA.
    bandera_d = False
    bandera_dr = False
    bandera_dre = False
    contador_palabras_dre = 0

    for car in cadena:
        # AFUERA DE LA PALABRA/AL FINAL. CONTAR PALABRAS AQUÍ.
        if car == " " or car == ".":
            # REALIZAR LOS SUBPROCESOS AQUÍ.
            if contador_letras > 0:
                contador_palabras += 1

                # Subproblema 1
                if contador_letras == 3:
                    contador_palabras_3_letras += 1

                # Subproblema 3
                if bandera_palabras_que_terminan_en_s == True:
                    contador_palabras_que_terminan_en_s += 1

                # Subproblema 4
                if bandera_dre == True:
                    contador_palabras_dre += 1




                # SECTOR REINICIO DE VARIABLES.
                bandera_palabras_que_terminan_en_s = False
                bandera_d = False
                bandera_dr = False
                bandera_dre = False
                contador_letras = 0



        # DENTRO DE LA PALABRA.
        else:
            contador_letras += 1

            # Subproblema 1

            # Subproblema 3
            ultimo_caracter = car
            if ultimo_caracter == "s":
                bandera_palabras_que_terminan_en_s = True

            # Subproblema 4
            if car == "d":
                bandera_d = True
                bandera_dr = False
            else:
                if bandera_d == True and car == "r":
                    bandera_dr = True
                else:
                    if bandera_dr == True and car == "e":
                        bandera_dre = True



    # Resultados

    # Subproblema 1
    print("La cantidad de palabras que presentan sólamente 3 letras, es de: ", contador_palabras_3_letras)

    # Subproblema 2
    porcentaje_3_letras = round(contador_palabras_3_letras * 100 / contador_palabras, 2)
    print("El porcentaje de palabras que representa el punto 1, es de: ", porcentaje_3_letras)

    # Subproblema 3
    print("La cantidad de palabras que terminan en \'s\' es de: ", contador_palabras_que_terminan_en_s)

    # Subproblema 4
    print("La cantidad de palabras que al menos tienen una vez la expresión \'dre\' es de: ",
          contador_palabras_dre)

program()
