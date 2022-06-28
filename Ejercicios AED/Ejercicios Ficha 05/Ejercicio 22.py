'''
Se vota una ley en el Senado, y se ingresan votos a favor, en contra y abstenciones de los senadores presentes.
Informar cuál fue el resultado de la votación. Si la ley fue aprobada,
indicar si fue por mayoría absoluta (más del 50% de los votos) o por mayoría simple.
Por último, considerando que la Cámara está formada por 72 senadores, determinar cuantos se encontraban ausentes.
'''

import random

random.seed(12)

# Constantes

# Entradas
votos_a_favor = random.randrange(1, 72)
votos_en_contra = random.randrange(1, votos_a_favor)
votos_en_blanco = random.randrange(1, votos_en_contra)

band_may_absoluta = False
band_may_simple = False

# Procesos
total_de_votos = votos_a_favor + votos_en_contra + votos_en_contra

porcentaje_aprobacion = votos_a_favor * 100 / total_de_votos
porcentaje_en_contra = votos_en_contra * 100 / total_de_votos
porcentaje_en_blanco = votos_en_blanco * 100 / total_de_votos

if votos_a_favor > votos_en_contra and votos_a_favor > votos_en_blanco:
    print("La ley fue aprobada, con un porcentaje de aprobación de: ", round(porcentaje_aprobacion, 2), "%")
    if porcentaje_aprobacion > 50:
        print("La ley fue aprobada por mayoría absoluta.")
    else:
        if porcentaje_aprobacion > 50 and porcentaje_aprobacion > porcentaje_en_contra \
            and porcentaje_aprobacion > porcentaje_en_blanco:
            print("La ley fue aprobada por mayoría simple.")

# Salidas
print(votos_a_favor)
print(votos_en_contra)
print(votos_en_blanco)
