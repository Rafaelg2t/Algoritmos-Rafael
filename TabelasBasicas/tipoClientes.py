from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def TipoClientesMenu():
    escolha = Menu("Tipo Clientes", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("TipoClientes", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("TipoClientes", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("TipoClientes", codigo)
        apagar_dados("TipoClientes")
    elif escolha==4:
        print_dados("TipoClientes")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("TipoClientes", valor)
