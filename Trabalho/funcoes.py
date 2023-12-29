import json


# Para teres noção do que são ficheiros json
# Em resumo, JSON é um formato de dados leve e legível por humanos, comumente usado para trocar informações entre sistemas. 
# Ele utiliza uma estrutura simples de pares chave-valor e suporta tipos de dados como strings, números, booleanos, arrays e objetos. 
# Sua simpliccodigoade e independência de linguagem o tornam amplamente utilizado na comunicação entre servcodigoores e clientes na web.
#
# Outra noção que tens de ter é objetos de json, que são pareccodigoos com dicionários de python (mais abaixo)
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
# Agora isto é pareccodigoo com dicionários em python por isso consegues usar isto à vontade, simples fazes o que tá na função
# carregar_dados() onde simplesmente usando a biblioteca devolve a variavel dados que podes usar como um dicionário.
# Um dicionário tem as chaves e o valor dentro da chave:
# {"chave": valor} 
#
#
# No teu codigo, assim como o meu e o do stor, estás a carregar o ficheiro json todo,
# isto é viável pelos ficheiros json serem pequenos e leves, sendo que foram feitos para tal por serem usados em sites, numa variável
# alteras a variável sendo ela um dicionário, e depois reescreves o ficheiro todo, já com as alterações feitas.


# Carregar ficheiro json
def carregar_dados():
    with open('dados.json', 'r') as file:
        dados = json.load(file)
        return dados


# Guardar ficheiro json
def guardar_dados(dados):
    with open('dados.json', 'w') as file:
        json.dump(dados, file)


# Apagar dado do ficheiro json
# Reescreve o ficheiro com tudo menos o dado que tem o codigo que se quer apagar 
def apagar_dados(codigo):
    dados = carregar_dados()
    dados = [dados for dados in dados if dados['codigo'] != codigo]
    guardar_dados(dados)


# Adiciona ao ficheiro json
# Dá "append" (adicionar) o dado que deste
def inserir_dado(dado):
    dados = carregar_dados()
    dados.append(dado)
    guardar_dados(dados)


# Agora tens mais um argumento, onde 
def inserir_dado(seccao, dado):
    dados = carregar_dados()
    dados[seccao].append(dado)
    guardar_dados(dados)


# Altera um valor
# Procura pelo codigo e quando encontra altera usando .update() um método onde altera o valor de uma chave
def alterar_dados(codigo, alterar_dados):
    dados = carregar_dados()
    for dados in dados:
        if dados['codigo'] == codigo:
            dados.update(alterar_dados)
            break
    guardar_dados(dados)

# Filtra os dados
# Procura pelos dados procurando por um valor dado
def filtrar_dados(filters):
    dados = carregar_dados()
    for key, value in filters.items():
        dados = [dados for dados in dados if dados[key] == value]
    return dados


# Print a tudo
# Simplesmente vai de linha em linha e da print
def print_dados():
    dados = carregar_dados()
    for dados in dados:
        print(dados)


# Exemplo de uso
# Apagar dado com codigo de 2
apagar_dados(2)
# Inserir dado
inserir_dado({"codigo": 5, "type": "Painel de Controle", "client": "Banco Inter", "dados": "Falha na aplicação", "date": "2021-06-25"})
# Alterar o "type" do dado com codigo de 1
alterar_dados(1, {"type": "Revisão de Segurança"})
# Vai dar print a todos os dados com "Banco Inter" de "client"
print(filtrar_dados({"client": "Banco Inter"}))
print_dados()





