def multa_localidade(v):
    if v <= 50:
        return 0
    elif v < 90:
        return 60
    elif v < 120:
        return 120
    else:
        return 320
    
def multa_fora_localidade(v):
    if v <= 90:
        return 0
    elif v < 120:
        return 60
    else:
        return 120
    
def multa_autoestrada(v):
    if v <= 120:
        return 0
    elif v <= 150:
        return 60
    elif v <= 175:
        return 120
    else:
        return 360
    
while True:

    print("\nCalcular multa de velocidade")
    print("1 - Localidade")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")
    print("0 - Sair")
    opção = input("Escolha a opção: ")

    if opção == '0':
        print("Programa encerrado.")
        break
    if opção not in ('1', '2', '3'):
        print("Opção inválida, tente novamente.")
        continue

    