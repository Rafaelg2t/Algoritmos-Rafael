from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def resultadosdeanalisesMenu():
    escolha = Menu("resultados de analises", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("resultadosdeanalises", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("resultadosdeanalises", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("resultadosdeanalises", codigo)
        apagar_dados("resultadosdeanalises")
    elif escolha==4:
        print_dados("resultadosdeanalises")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("resultadosdeanalises", valor)
    