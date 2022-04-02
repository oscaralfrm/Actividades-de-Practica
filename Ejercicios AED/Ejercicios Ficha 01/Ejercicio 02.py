# Un binomioal cuadrado (suma) esigual al cuadrado del primer término,
# más el doble producto del primero por el segundo más el cuadradod del segundo.

# Plantear un script directamente en el shell de Python, que permita mostrar,
# para dos valores a y b, el valor del cuadrado del binomio.

# Entradas

a = int(input("Primer número del binomio:"))
b = int(input("Segundo número del binomio:"))

# Procesos
primer_elemento_al_cuadrado = int(a**2)
doble_del_producto = (2 * a * b)
segundo_elemento_al_cuadrado = int(b**2)
resultado_binomio_cuadrado_perfecto = (primer_elemento_al_cuadrado + doble_del_producto + segundo_elemento_al_cuadrado)

# Salidas
print("El binomio a continuación se representa como: ", primer_elemento_al_cuadrado,"+",doble_del_producto,"+",segundo_elemento_al_cuadrado)
print("El valor del cuadrado del binomio es: ", resultado_binomio_cuadrado_perfecto)
