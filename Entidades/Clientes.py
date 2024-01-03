from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def ClientesMenu():
    escolha = Menu("Clientes", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("Clientes", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("Clientes", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("Clientes", codigo)
        apagar_dados("Clientes")
    elif escolha==4:
        print_dados("Clientes")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("Clientes", valor)
