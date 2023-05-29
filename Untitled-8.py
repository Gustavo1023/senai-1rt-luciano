def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

def menor_numero(a, b):
    if a < b:
        return a
    else:
        return b

# Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior número")
    print("d. Menor número")

# Programa principal
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

exibir_menu()
opcao = input("Digite a opção desejada: ")

if opcao == "a":
    resultado = somar(valor1, valor2)
    print("Resultado da soma:", resultado)
elif opcao == "b":
    resultado = multiplicar(valor1, valor2)
    print("Resultado da multiplicação:", resultado)
elif opcao == "c":
    resultado = maior_numero(valor1, valor2)
    print("Maior número:", resultado)
elif opcao == "d":
    resultado = menor_numero(valor1, valor2)
    print("Menor número:", resultado)
else:
    print("Opção inválida!")
    