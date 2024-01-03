from Funcoes.funcoes import *
from Funcoes.menu import *
from Funcoes.valores import *

def FuncionariosMenu():
    escolha = Menu("Funcionarios", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])
    
    if escolha==1:
        dadoAInserir = {}
        dadoAInserir["Codigo"] = pedirCodigo()
        dadoAInserir["Nome"] = pedirNome()
        inserir_dado("Funcionarios", dadoAInserir)
    elif escolha==2:
        codigo = pedirCodigo()
        alterar_dados("Funcionarios", codigo)
    elif escolha==3:
        codigo = pedirCodigo()
        alterar_dados("Funcionarios", codigo)
        apagar_dados("Funcionarios")
    elif escolha==4:
        print_dados("Funcionarios")
    elif escolha==5:
        valor = pedirNome()
        filtrar_dados("Funcionarios", valor)
