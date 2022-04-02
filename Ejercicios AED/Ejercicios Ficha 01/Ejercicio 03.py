# Desarrolle un programa para calcular el área de un triángulo,
# cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.
# (Observar que la altura no es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).

# Menu
print("Cálculo del área de un triángulo")

# Entradas

b = int(input("Valor de la base: "))

# Procesos
altura = int(b**2)
area_de_un_triangulo = (b * altura) // 2

# Salidas
print("El área del triángulo es:", area_de_un_triangulo)
