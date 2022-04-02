# Conociendo el precio de lista de un artículo, determinar:
# Precio de venta al contado (10% de descuento)
# Precio de venta con tarjeta (5% de recargo)

# Menu
print("Cálculo de precio de venta al contado y con tarjeta: ")

# Entradas
valor_producto = float(input("Ingrese el precio del producto: "))

# Constantes
DESCUENTO_AL_CONTADO = valor_producto * 0.1  # Restar al valor total.
IMPUESTO_POR_TARJETA = valor_producto * 0.05  # Sumar al valor total.

# Procesos
precio_venta_al_contado = valor_producto - DESCUENTO_AL_CONTADO
precio_venta_por_tarjeta = valor_producto + IMPUESTO_POR_TARJETA

# Salidas
print("El precio total del producto al contado es de: ", precio_venta_al_contado)
print("El precio total del producto por tarjeta es de: ", precio_venta_por_tarjeta)
