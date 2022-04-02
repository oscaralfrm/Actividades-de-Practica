# ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
# ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado)
# y los dos últimos dígitos (por otro lado)
# [Ayuda: ¿cuáles son los posibles restos que se obtienen de dividir un número cualquiera por 10?]

# Menu
print("Sacando los 2 últimos dígitos... usando el operador módulo.")

# Entradas

valor_entero = int(input("Ingrese un valor de cualquier número entero: "))

# Procesos
eliminador_del_ultimo_digito = valor_entero % 10
eliminador_de_los_dos_ultimos_digitos = valor_entero % 100

# Salidas
print("El último dígito de", valor_entero, "es", eliminador_del_ultimo_digito)
print("Los 2 últimos dígitos de", valor_entero, "son", eliminador_de_los_dos_ultimos_digitos)
