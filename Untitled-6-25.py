while True:
    numero = int(input("Digite um número (ou um valor negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break
    
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")