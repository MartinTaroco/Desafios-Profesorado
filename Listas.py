#Forma uno, con funciones integradas
notas = [2 , 4, 5, 6, 1]

suma_notas= sum(notas)   #Suma todas las notas
cantidad_notas= len(notas)  #muestra la cantidad de elementos de una lista
notas_maximo = max(notas)   #Da el elemento maximo de una lista de números
notas_minimo = min(notas)    #Da el elemento minimo de una lista de números

promedio_notas = suma_notas / cantidad_notas

print(promedio_notas)
print (notas_maximo)
print (notas_minimo)

#Forma dos, metodos y for

suma_notas = 0
for i in notas:
  suma_notas += i             #Sumamos todas las notas

promedio_notas = suma_notas / cantidad_notas

print(promedio_notas)

#Para nota mas alta y mas baja, ordenamos la lista de menor a mayor
notas.sort()


notas_maximo = notas [-1]   #Mostramos la ultima nota por su indice
notas_minimo = notas[0]      #Mostramos la primera nota por su indice

print(notas_maximo)
print(notas_minimo)

