# Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una
# dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:
# Componer la dirección de correo de la siguiente manera:
# <primera letra del nombre><apellido>@<dominio>
# Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería:
# fsteffolani@frc.utn.edu.ar
# Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
# <nombre>.<apellido>@<dominio>
# Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
# soledad.steffolani@colegiorosarito.edu.ar

# Menu
print('*' * 50)
print("* \tGenerador de Correos Electrónicos: *")
print('*' * 50)


# Constante
DOMINIO = "@frc.utn.edu.ar"

# Entradas
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
nombre_usuario_minuscula = nombre_usuario.lower()
apellido_usuario_minuscula = apellido_usuario.lower()

# Procesos
if nombre_usuario[0] != apellido_usuario[0]:
    print("Su correo electrónico es: " + nombre_usuario_minuscula[0] + apellido_usuario_minuscula + DOMINIO)
else:
    if nombre_usuario[0] == apellido_usuario[0]:
        print("Su correo electrónico es: " + nombre_usuario_minuscula + "." + apellido_usuario_minuscula + DOMINIO)

