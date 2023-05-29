distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco_passagem = distancia * 0.50  # R$0,50 por km para viagens até 200 km
else:
    preco_passagem = distancia * 0.45  # R$0,45 por km para viagens acima de 200 km

print(f"O preço da passagem é R$ {preco_passagem:.2f}.")
