# Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista.
# La distancia aproximada entre ambas ciudades es de 400 kilómetros.
# El vehículo se desplaza con velocidad promedio de 122 km/h.
# Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Rosario.
# De nuevo, no es necesario convertir a horas, minutos y segundos:
# exprese en resultado como un número real,
# tal cual lo haya obtenido del cálculo.

# Menu
print("¿Cuánto tardo en llegar desde Córdoba a Rosario?")

# Entradas
'''
No hay entradas especiales por teclado debido a que el ejercicio se resuelve desde el apartado de procesos.
'''
distancia_cordoba_rosario = 400
velocidad_promedio_vehiculo = 122

# Procesos
'''
Hay que pensar en la fórmula de V = d / t ; hacer un despeje, que nos quedaría:
t = d / V.
En donde t es el tiempo que tarda en llegar el vehículo desde Córdoba a Rosario.
d es la distancia, medida en metros.
V es la velocidad promedio del viaje.
'''
tiempo_de_llegada = distancia_cordoba_rosario / velocidad_promedio_vehiculo

# Salidas
print("El tiempo estimado de llegada es:", tiempo_de_llegada, "horas.")
