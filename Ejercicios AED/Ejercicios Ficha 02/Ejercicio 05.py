# Se sabe que la suma de dos ángulos desconocidos (alfa + beta)
# es igual a cierto valor x que se carga por teclado. Además se sabe que la diferencia entre esos mismos
# dos ángulos (alfa - beta) es igual a otro valor y que también se carga por teclado.
# Desarrolle un programa que dados los valores x e y, determine el valor de los dos ángulos alfa y beta.
# No es necesario convertir a grados, minutos y segundos el valor de cada ángulo:
# expréselos como números reales, tal cual hayan sido obtenidos.

# Menu
print("Calcular los valores de alfa y beta:")

# Entradas
x = int(input("Ingrese el valor de la variable x: "))
y = int(input("Ingrese el valor de la variable y: "))


# Procesos
'''Hay que plantear en definitiva un sistema de ecuaciones, reemplazando valores. Supongamos que:
alfa + beta = 90 (x)
alfa = 90 - beta

alfa – beta = 60 (y)
alfa = 60 + beta

90 – beta = 60 + beta
90 – 60 = beta**2
Raíz cuadrada de 30 = beta

Reemplazando beta en la primer afórmula...
alfa = 90 - beta

Por lo que podríamos resolver el ejercicio planteándolo por método de sustición.
'''
beta = ((x - y)**0.5)
alfa = x - beta

# Salidas
print("El valor de x es: ", x)
print("El valor de y es: ", y)
print("El valor de alfa es: ", alfa)
print("El valor de beta es: ", beta)
