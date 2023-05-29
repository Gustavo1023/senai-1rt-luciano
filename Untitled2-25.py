numero = int(input("Digite um número: "))
fatorial = 1

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}.")