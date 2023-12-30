class bcolors:
    HEADER = '[95m'
    OKBLUE = '[94m'
    OKCYAN = '[96m'
    OKGREEN = '[92m'
    WARNING = '[93m'
    FAIL = '[91m'
    ENDC = '[0m'
    BOLD = '[1m'
    UNDERLINE = '[4m'
    NORMAL = '[00m'


def print2(cor, prt):
    print(f"{cor}{prt}{bcolors.NORMAL}")


def Menu(Titulo, Opcoes):
    print2(bcolors.OKBLUE, "* " * 5 + Titulo + " *" * 5)
    print()
    numeroOpcoes = len(Opcoes)
    for i in range(numeroOpcoes):
        print(i + 1, "-", Opcoes[i])
    print("0 - Terminar")
    while True:
        try:
            op = int(input("Opção?"))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if op >= 0 and op <= numeroOpcoes:
            break
        else:
            print("O valor deve estar entre %d e %d" % (0, numeroOpcoes))
    return op
