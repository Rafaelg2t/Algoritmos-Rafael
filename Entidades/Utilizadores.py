from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def UtilizadoresMenu():
    escolha = Menu("Utilizadores", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("Utilizadores", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("Utilizadores", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("Utilizadores", codigo)
        apagar_dados("Utilizadores")
    elif escolha==4:
        print_dados("Utilizadores")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("Utilizadores", valor)
