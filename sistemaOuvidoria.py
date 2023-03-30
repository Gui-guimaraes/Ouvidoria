from operacoesbd import *
# Sistema de ouvidoria

class Reclamacao:
    def __init__(self, nome, assunto, mensagem):
        self.nome = nome
        self.assunto = assunto
        self.mensagem = mensagem

# Menu de opções
def menu():
    print('Ola! seja bem-vindo a ouvidoria')
    print('1 - Registrar reclamação')
    print('2 - Listar reclamações')
    print('3 - Pesquisar reclamação por código')
    print('4 - Remover reclamação')
    print('5 - Sair')
    opcao = int(input('Digite a opção desejada: ')) 
    return opcao

# Obter dados do usuário
def obterDados():
    conexao = abrirBancoDados('localhost','root','Eacpncdmn3@2','ouvidoria')
    nome = input("Digite seu nome: ")
    assunto = input("Digite o assunto da reclamação: ")
    mensagem = input("Digite a mensagem da reclamação: ")
    inserirReclamacao = 'insert into sistema_ouvidoria (nome, assunto, mensagem) values (%s, %s, %s)'
    dados = (nome, assunto, mensagem)
    insertNoBancoDados(conexao, inserirReclamacao, dados)
    return Reclamacao(nome, assunto, mensagem)

    encerrarBancoDados(conexao)

# Pesquisar reclamação por código
def pesquisarCodigo(reclamacoes):
        conexao = abrirBancoDados('localhost','root','Eacpncdmn3@2','ouvidoria')
        listarReclamacoes(reclamacoes)
        print('Pesquisar reclamação por código')
        print()
        codigo = input('Digite o código da reclamação a ser pesquisada: ')
        consultarReclamacao = 'select nome, assunto, mensagem from sistema_ouvidoria where codigo_reclamacao = ' + codigo
        pesquisarReclamacao = listarBancoDados(conexao, consultarReclamacao)
        if len(pesquisarReclamacao) == 0:
            print('Não há reclamações registradas')
        else:
            print()
            print('Pesquisando reclamação...')
            for reclamacao in pesquisarReclamacao:
                print('Nome: ', reclamacao[0])
                print('Assunto: ', reclamacao[1])
                print('Mensagem: ', reclamacao[2])
        encerrarBancoDados(conexao)

# Sistema de admin

class Admin:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

admin = [Admin("admin", "admin")]

def autenticar(self, login, senha):
    for adm in admin:
        if adm.login == login and adm.senha == senha:
            return True
    return False

# Funções do Admin

# Listar reclamações 

def listarReclamacoes(reclamacoes):
    conexao = abrirBancoDados('localhost','root','Eacpncdmn3@2','ouvidoria')
    # Listar reclamações
    consultarListagem = 'select * from sistema_ouvidoria'
    listaReclamacao = listarBancoDados(conexao, consultarListagem)
    if len(listaReclamacao) == 0:
        print('Não há reclamações registradas')
    else:
        print()
        print('Listando reclamações...')
        for reclamacao in listaReclamacao:
            print('Código: ', reclamacao[0])
            print('Nome: ', reclamacao[1])
            print('Assunto: ', reclamacao[3])
            print('Mensagem: ', reclamacao[4])
            print()
    encerrarBancoDados(conexao)
 

# Remover reclamações e dados do usuário

def removerReclamacoes():
    conexao = abrirBancoDados('localhost','root','Eacpncdmn3@2','ouvidoria')
    codigo = input('Digite o código da reclamação a ser removida: ')
    remover_reclamacao = 'delete from sistema_ouvidoria where codigo_reclamacao = %s'
    dados = (codigo,)
    excluirBancoDados(conexao, remover_reclamacao, dados)
    encerrarBancoDados(conexao)


