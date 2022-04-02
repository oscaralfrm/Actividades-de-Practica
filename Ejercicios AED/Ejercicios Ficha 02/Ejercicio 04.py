# Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de
# segundo grado, y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
# Además, para el mismo polinomio, calcule y muestre el valor del
# discriminante de la fórmula para el cálculo de las raíces de la ecuación.

# Menu
print("Cálculo de polinomio de segundo grado:")

# Entradas
a = int(input("Ingrese el valor del coeficiente a: "))
b = int(input("Ingrese el valor del coeficiente b: "))
c = int(input("Ingrese el valor del coeficiente c: "))
x = int(input("Ingrese el valor de la variable x: "))

# Procesos
ecuacion_valor_polinomio_segundo_grado = a*x**2 + b*x + c
valor_discriminante_bhaskara = (b**2 - 4 * a * c)  # Se usará para corroborar el valor de x.
discriminante_bhaskara_con_raiz = ((b**2 - 4 * a * c)**0.5)  # Se usará como subproceso de la fórmula.
formula_de_bhaskara_cuando_x_es_positiva = (-b + discriminante_bhaskara_con_raiz) / 2 * a
formula_de_bhaskara_cuando_x_es_negativa = (-b - discriminante_bhaskara_con_raiz) / 2 * a


# Salidas
print("El valor del polinomio de segundo grado es de: ", ecuacion_valor_polinomio_segundo_grado)
print("El valor de la discriminante es: ", valor_discriminante_bhaskara)
print("El valor del primer corte en X (primera raíz) es de: ", formula_de_bhaskara_cuando_x_es_positiva)
print("El valor del segundo corte en X (segunda raíz) es de: ", formula_de_bhaskara_cuando_x_es_negativa)
