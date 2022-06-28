'''
13. Silaba "ta"
El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero.
La frase finaliza con un punto, y las palabras están separadas por espacios únicamente.
Se debe mostrar:

a) Ver el porcentaje de vocales respecto del total de letras de la frase.

b) La longitud promedio de las palabras

c) La longitud de la palabra mas larga del texto

d) Cantidad de palabras que comienzan con "ta"

'''

def validar_vocales(caracter):
    vocales = ('aeiouáéíóú')
    if caracter in vocales:
        return vocales

def programa():
    cadena = input("Ingrese un texto: ")
    cadena.lower()
    contador_letras = 0
    contador_palabras = 0
    palabra_mayor = " "
    palabra_menor = " "

    # Subproblema 1:
    contador_vocales = 0

    # Subproblema 2:
    # Dividir el contador de letras sobre el contador de palabras.

    # Subproblema 3:
    # Usar bandera para detectar y comparar la palabra más larga del texto, dada por el contador de letras.
    # Ir comparando, cantidad de letras de una palabra con la cantidad de letras de otra.

    # Subproblema 4:
    # Usar banderas y contador_letras para identificar cuando comienzan con 'ta'.
    bandera_t = False
    bandera_ta = False
    contador_palabras_comienzan_ta = 0

    for car in cadena:
        # AFUERA/AL FINAL DE LA PALABRA.
        if car == " " or car == ".":
            # SECTOR PROCESADO DE PALABRAS (DENTRO DE ESTE IF).
            if contador_letras > 1:
                contador_palabras += 1

                # Subproblema 3

                # Subproblema 4
                if bandera_ta is True:
                    contador_palabras_comienzan_ta += 1


            # SECTOR REINICIO:
            bandera_ta = False
            bandera_t = False

        # ADENTRO DE LA PALABRA:
        else:
            contador_letras += 1
            # Subproblema 1
            if validar_vocales(car):
                contador_vocales += 1


            # Subproblema 2
            # Se resuelve en el apartado de Resultados.


            # Subproblema 3
            # Se plantea en el apartado de AL FINAL DE LA PALABRA.
            if palabra_mayor > palabra_menor:
                palabra_mayor = palabra_mayor
            else:
                palabra_mayor = palabra_menor

            # Subproblema 4
            if contador_letras == 1:
                if car == "t":
                    bandera_t = True
            if contador_letras == 2:
                if bandera_t == True and car == "a":
                    bandera_ta = True





    # Resultados
    # Subproblema 1
    porcentaje_vocales = contador_vocales * 100 / contador_letras
    print("El porcentaje de vocales respecto al total de letras de la frase es de: ", porcentaje_vocales)

    # Subproblema 2
    longitud_promedio = contador_letras / contador_palabras
    print("La longitud promedio de las palabras es de: ", longitud_promedio)

    # Subproblema 3

    # Subproblema 4
    print("La cantidad de palabras que comienzan con \'ta\' es de: ", contador_palabras_comienzan_ta)


programa()
