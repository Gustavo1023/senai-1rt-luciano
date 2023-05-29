velocidade = float(input("Digite a velocidade do carro em km/h: "))
limite_velocidade = 80
valor_multa_por_km = 7.00

if velocidade > limite_velocidade:
    velocidade_excedida = velocidade - limite_velocidade
    valor_multa = velocidade_excedida * valor_multa_por_km
    print("Você foi multado!")
    print("Velocidade excedida: {:.2f} km/h".format(velocidade_excedida))
    print("Valor da multa: R$ {:.2f}".format(valor_multa))
else:
    print("Você está dentro do limite de velocidade.")