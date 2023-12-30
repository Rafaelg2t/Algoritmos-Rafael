def pedirCodigo():
    while True:
        numero = input("Digite um codigo")
        try:
            return int(numero)
        except:
            print("Precisa de ser um número!")


def pedirNome():
    print("Por fazer")
    