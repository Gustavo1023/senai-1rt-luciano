salario = float(input("Digite o salário do funcionário: "))

if salario > 8250.00:
    aumento = salario * 0.10  # Aumento de 10% para salários superiores a R$8.250,00
else:
    aumento = salario * 0.15  # Aumento de 15% para salários iguais ou inferiores a R$8.250,00

novo_salario = salario + aumento

print(f"O valor do aumento é R$ {aumento:.2f}.")
print(f"O novo salário é R$ {novo_salario:.2f}.")


