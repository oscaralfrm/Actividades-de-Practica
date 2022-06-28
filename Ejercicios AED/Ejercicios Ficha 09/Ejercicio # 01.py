'''
Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos
opciones: una es cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla
con un for iterador; y la otra es cargar cada caracter uno por uno a través de un while).
Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada
palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

1) Determinar cuántas palabras tenían más de 4 letras.

2) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

3) Determinar el promedio de letras por palabra en todo el texto.

4) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".
'''

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Análisis de Texto')
print('*' * 80)

#Inicialización
letras_pal = 0
palabras_mas4 = 0
tieneXY = False
palabras_XY = 0
letras = 0
palabras = 0
anterior = None
cantMO = 0
palabras_MO = 0

#Carga de datos y proceso
texto = input('Ingrese el texto, separando palabras con un espacio y terminando con punto:')
for letra in texto:
    if letra == ' ' or letra == '.':
        #La longitud es mayor a 4?
        if letras_pal > 4:
            palabras_mas4 += 1
        #Contar si tiene X o Y
        if tieneXY == True:
            palabras_XY  += 1
        #Contar la palabra si ya se cargó algún caracter
        if letras >0:
            palabras += 1
        #Contar la palabra si tiene un solo MO
        if cantMO == 1:
            palabras_MO += 1
        #Reiniciar datos de la palabra
        letras_pal = 0
        tieneXY = False
        cantMO = 0
    else:
        #Procesando palabra
        letras_pal += 1
        #Detectar X o Y
        if letra == 'x' or letra == 'y':
            tieneXY = True
        #Contar todas las letras del texto
        letras += 1
        #Detectar la expresión MO
        if letra == 'o' and anterior == 'm':
            cantMO += 1
    anterior = letra

#Resultados
print('*' * 80)
print('Palabras con más de 4 letras:',palabras_mas4)
print('Palabras tenían al menos una vez la letra "x" o la letra "y":',palabras_XY)
if palabras == 0:
    promedio = 0
else:
    promedio = round(letras / palabras, 2)
print('El promedio de letras por palabra en todo el texto es:',promedio)
print('Determinar cuántas palabras contuvieron sólo una vez la expresión "mo":',palabras_MO)
