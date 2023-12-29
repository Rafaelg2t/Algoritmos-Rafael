import json


# Para teres noção do que são ficheiros json
# Em resumo, JSON é um formato de dados leve e legível por humanos, comumente usado para trocar informações entre sistemas. 
# Ele utiliza uma estrutura simples de pares chave-valor e suporta tipos de dados como strings, números, booleanos, arrays e objetos. 
# Sua simplicidade e independência de linguagem o tornam amplamente utilizado na comunicação entre servidores e clientes na web.
#
# Outra noção que tens de ter é objetos de json, que são parecidos com dicionários de python (mais abaixo)
# Exemplo de um objeto de objeto de um ficheiro json, que começa e acaba com os "{}"":
#
#{
#  "name": "John Doe",  <-- Chave com uma string como valor
#  "age": 30,   <-- Chave com um int (integer, número inteiro) como valor
#  "city": "Exampleville", 
#  "isStudent": false, <-- Chave com um valor booleano (verdadeiro ou falso) como valor
#  "hobbies": ["reading", "coding", "traveling"]    <-- Chave com um array como valor
#}
#
# Agora isto é parecido com dicionários em python por isso consegues usar isto à vontade, simples fazes o que tá na função
# carrgar_dados() onde simplesmente usando a biblioteca devolve a variavel dados que podes usar como um dicionário.
# Um dicionário tem as chaves e o valor dentro da chave:
# {"chave": valor} 
#
#
# No teu codigo, assim como o meu e o do stor, estás a carregar o ficheiro json todo,
# isto é viável pelos ficheiros json serem pequenos e leves, sendo que foram feitos para tal por serem usados em sites, numa variável
# alteras a variável sendo ela um dicionário, e depois reescreves o ficheiro todo, já com as alterações feitas.

'''
Tenta dar rename nas funções pra tar tudo me portugues
'''
'''
Fiz alguma cena!
'''
# Carregar ficheiro json
def carrgar_dados():
    with open('dados.json', 'r') as file:
        dados = json.load(file)
        return dados

# Guardar ficheiro json
def guardar_dados(dados):
    with open('dados.json', 'w') as file:
        json.dump(dados, file)

# Apagar dado do ficheiro json
# Reescreve o ficheiro com tudo menos o dado que tem o id que se quer apagar 
def apagar_dados(id):
    dados = carrgar_dados()
    dados = [dados for dados in dados if dados['id'] != id]
    guardar_dados(dados)

# Adiciona ao ficheiro json
# Dá "append" (adicionar) o dado que deste
def inserir_Dado(dado):
    dados = carrgar_dados()
    dados.append(dado)
    guardar_dados(dados)

# Agora tens mais um argumento, onde 
def inserirDado(seccao, dado):
    dados = carrgar_dados()
    dados[seccao].append(dado)
    guardar_dados(dados)


try:
    print("A tentar fazer algo")
except:
    print("Deu erro, a resolver")


# Altera um valor
# Procura pelo id e quando encontra altera usando .update() um método onde altera o valor de uma chave
def alterar_dados(id, alterar_dados):
    dados = carrgar_dados()
    for dados in dados:
        if dados['id'] == id:
            dados.update(alterar_dados)
            break
    guardar_dados(dados)

# Filtra os dados
# Procura pelos dados procurando por um valor dado
def filtrar_dados(filters):
    dados = carrgar_dados()
    for key, value in filters.items():
        dados = [dados for dados in dados if dados[key] == value]
    return dados

# Print a tudo
# Simplesmente vai de linha em linha e da print
def print_dados():
    dados = carrgar_dados()
    for dados in dados:
        print(dados)

# Exemplo de uso
# Apagar dado com id de 2
apagar_dados(2)
# Inserir dado
inserir_Dado({"id": 5, "type": "Painel de Controle", "client": "Banco Inter", "dados": "Falha na aplicação", "date": "2021-06-25"})
# Alterar o "type" do dado com id de 1
alterar_dados(1, {"type": "Revisão de Segurança"})
# Vai dar print a todos os dados com "Banco Inter" de "client"
print(filtrar_dados({"client": "Banco Inter"}))
print_dados()





