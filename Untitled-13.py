from time import sleep
def contagem_regressiva(cont):
    while cont > 0:
        print(cont)
        cont = cont - 1
        sleep (1)



p = int(input("digite um valor de contagem: "))
contagem_regressiva(p)