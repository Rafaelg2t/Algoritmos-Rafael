from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def TipoAnalisesMenu():
    escolha = Menu("Tipo Analises", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("TipoAnalises", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("TipoAnalises", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("TipoAnalises", codigo)
        apagar_dados("TipoAnalises")
    elif escolha==4:
        print_dados("TipoAnalises")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("TipoAnalises", valor)
    
