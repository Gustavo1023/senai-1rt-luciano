valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = valor1 + valor2
    operacao = "adição"
elif opcao == 2:
    resultado = valor1 - valor2
    operacao = "subtração"
elif opcao == 3:
    resultado = valor1 / valor2
    operacao = "divisão"
elif opcao == 4:
    resultado = valor1 * valor2
    operacao = "multiplicação"
else:
    print("Opção inválida.")
    exit()

print("Resultado da {} entre {} e {}: {}".format(operacao, valor1, valor2, resultado))
