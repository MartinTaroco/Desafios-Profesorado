#Desafio 3 : Identificador de Palindromos


def es_palindromo(palabra):
  lista_palabra = []
  
  for i in palabra:
    lista_palabra.append(i)

  inversa = lista_palabra[::-1]
  
  if lista_palabra == inversa:
    print(True)
  else:
    print(False)
    

resultado = es_palindromo("gato")

print(resultado)

#Codigo mucho mas limpio
def es_palindromo(palabra):
    return list(palabra) == list(palabra[::-1])

print(es_palindromo("arenera"))  # True