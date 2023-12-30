from Funcoes.funcoes import *
from TabelasBasicas.tipoClientes import *
from Funcoes.valores import *
opcao = Menu("Gesteor de laboratório", ["Tabelas básicas", "Entidades", "Análises"])


escolha = Menu("Tipo Clientes", ["Inserir", "Alterar", "Eliminar", "Mostrar tudo", "Mostar com filtro"])

if escolha==1:
    dadoAInserir = {}
    dadoAInserir["Codigo"] = pedirCodigo()
    dadoAInserir["Nome"] = pedirNome()
    inserir_dado("TipoClientes", dadoAInserir)
elif escolha==2:alterar_dados("TipoClientes")
elif escolha==3:apagar_dados("TipoClientes")
elif escolha==4:print_dados("TipoClientes")
elif escolha==5:filtrar_dados("TipoClientes", valor)