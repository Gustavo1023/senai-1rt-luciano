def contagem_regressiva (numero):
  if numero <= 0:
   print ("O numero tem que ser maior que zero")
   return

for i in range (numero, -1, -1):
  print (i)

contagem_regressiva (8)