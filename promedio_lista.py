#Escribe una función recursiva que calcule el promedio de los elementos de una lista de enteros.



def promedio(lista):
 promedio = sum(lista) / len(lista)    #Calculo el promedo total suma / cantidad elementos
 return promedio

resultado = promedio([1,3])

print(resultado)