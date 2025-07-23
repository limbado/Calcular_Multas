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

    velocidade = float(input("Digite a velocidade do carro (km/h): "))

    if velocidade < 50:
        print("Sem multa. Velocidade dentro do permitido.")
        continue

    if opção == '1':
        multa = multa_localidade(velocidade)
    elif opção == '2':
        multa = multa_fora_localidade(velocidade)
    else:
        multa = multa_autoestrada(velocidade)

    print(f"Multa a pagar: {multa}€")
