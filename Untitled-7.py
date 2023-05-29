def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(verificar_par(4))    # True
print(verificar_par(7))    # False
print(verificar_par(0))    # True
print(verificar_par(-2))   # True
