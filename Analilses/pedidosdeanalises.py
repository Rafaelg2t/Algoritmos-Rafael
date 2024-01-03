from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def PedidosdeanalisesMenu():
    escolha = Menu("Pedidos de analises", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("Pedidosdeanalises", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("Pedidosdeanalises", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("Pedidosdeanalises", codigo)
        apagar_dados("Pedidosdeanalises")
    elif escolha==4:
        print_dados("Pedidosdeanalises")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("Pedidosdeanalises", valor)
