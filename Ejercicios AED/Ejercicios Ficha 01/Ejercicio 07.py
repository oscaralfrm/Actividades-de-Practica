# Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
# Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
# más un valor extra calculado en base de la cantidad de kilómetros a recorrer:
# Por cada kilómetro a recorrer se cobra $0.30 de adicional.

# Menu
print("Calculadora precio boleto de ómnibus:")

# Entradas
monto_base_boleto = float(input("Ingrese el monto base a pagar: "))
kilometros_de_viaje = float(input("Ingrese cuántos kilómetros va a viajar: "))

# Procesos
valor_pasaje_omnibus = monto_base_boleto + (0.30 * kilometros_de_viaje)


# Salidas
print("El valor total del pasaje de omnibus es de", valor_pasaje_omnibus)
