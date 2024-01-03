from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def AnalisesMenu():
    escolha = Menu("Analises", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("Analises", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("Analises", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("Analises", codigo)
        apagar_dados("Analises")
    elif escolha==4:
        print_dados("Analises")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("Analises", valor)
