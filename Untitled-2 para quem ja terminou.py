porcentagem_nota = float(input("Digite a porcentagem da nota obtida: "))

if porcentagem_nota <= 50:
    premio = "Certificado de Participação"
elif porcentagem_nota <= 60:
    premio = "Certificado de Menção Honrosa"
elif porcentagem_nota <= 70:
    premio = "Medalha de Bronze"
elif porcentagem_nota <= 90:
    premio = "Medalha de Prata"
else:
    premio = "Medalha de Ouro"

print("Prêmio obtido: {}".format(premio))