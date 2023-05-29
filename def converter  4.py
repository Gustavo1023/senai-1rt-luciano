def converter_para_centimetros(valor_metros):
    return valor_metros * 100

def converter_para_milimetros(valor_metros):
    return valor_metros * 1000

valor_metros = float(input("Digite um valor em metros: "))

valor_centimetros = converter_para_centimetros(valor_metros)
valor_milimetros = converter_para_milimetros(valor_metros)

print(f"{valor_metros} metros equivalem a {valor_centimetros} centímetros.")
print(f"{valor_metros} metros equivalem a {valor_milimetros} milímetros.")
