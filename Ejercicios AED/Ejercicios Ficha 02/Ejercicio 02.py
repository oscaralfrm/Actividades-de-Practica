# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
# (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%.
# Mostrar el precio actual, el monto del descuento y el monto final a pagar.

# Menu
print("Descuento y monto a pagar por medicamento en farmacias Líder:")

# Entradas
precio_medicamento = float(input("Ingrese el precio del medicamento:"))

# Procesos
descuento_de_medicamentos = (precio_medicamento * 0.35)
monto_final_a_pagar = precio_medicamento + descuento_de_medicamentos


# Salidas
print("El precio del medicamento es de: ", precio_medicamento)
print("El descuento del medicamento es de: ", descuento_de_medicamentos)
print("El monto total a pagar por su medicamento es de: ", monto_final_a_pagar)
