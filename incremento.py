#Crea una función que reciba un entero como argumento y devuelva su valor incrementado en 1.

def incrementador(n):
  
  if isinstance(n, str):
    print("Digitaste un texto")
  elif n != int(n):
    print("No digitaste un entero")
  else:
   n += 1              #Incrementa el número
   return n


resultado = incrementador("Ho")
print (resultado)