#Escribir un programa en Python que calcule el seno de un ángulo en radianes usando la función math.sin.

import math #Importo el múdulo math



angulo_radian = math.radians(float(input("Escribe el ángulo para la función seno: "))) #EL usuario coloca el angulo en grados y se transforma a radianes
resultado = math.sin(angulo_radian)   #Se calcula el seno del angulo aportado

print("Seno del ángulo:", resultado)