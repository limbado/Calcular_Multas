def multa_localidade(v):
    if v <= 50:
        return 0
    elif v < 90:
        return 60
    elif v < 120:
        return 120
    else:
        return 320
