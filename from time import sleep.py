from time import sleep

def contagem_regressiva(nu):
  while nu > 0:
    nu = nu - 1
    print (nu)
    sleep (1)
    
p = int(input("declare o valor inicial: "))

contagem_regressiva(p)