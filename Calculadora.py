#Desafio 4: Creear una calculadora

def calculadora(a,b, operacion):
  num = 0
  op = str(operacion)
  if op == "+":
     num = a + b
  elif op == "-":
   num = a - b 
  elif op == "*":
    num = a * b  
  return num


cuenta = calculadora(2,4,"*")

print(cuenta)

