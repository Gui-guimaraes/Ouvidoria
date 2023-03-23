from operacoesbd import *
# Sistema de ouvidoria

class Reclamacao:
    def __init__(self, nome, email, assunto, mensagem):
        self.nome = nome
        self.email = email
        self.assunto = assunto
        self.mensagem = mensagem


def obterDados():
    conexao = abrirBancoDados('localhost','root','password','ouvidoria')

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    assunto = input("Digite o assunto da reclamação: ")
    mensagem = input("Digite a mensagem da reclamação: ")
    inserirReclamacao = 'insert into sistema_ouvidoria (nome, email, assunto, mensagem) values (%s, %s, %s, %s)'
    dados = (nome, email, assunto, mensagem)
    insertNoBancoDados(conexao, inserirReclamacao, dados)
    return Reclamacao(nome, email, assunto, mensagem)

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

# Listar reclamações e/ou dados do usuário

def listarReclamacoes():
    conexao = abrirBancoDados('localhost','root','password','ouvidoria')
    # Listar reclamações
    consultarListagem = 'select * from sistema_ouvidoria'
    listaReclamacao = listarBancoDados(conexao, consultarListagem)
    for reclamacao in listaReclamacao:
        print('Código: ', reclamacao[0])
        print('Nome: ', reclamacao[1])
        print('Email: ', reclamacao[2])
        print('Assunto: ', reclamacao[3])
        print('Mensagem: ', reclamacao[4])
        print()
    encerrarBancoDados(conexao)
 
# Atualizar reclamações ou dados do usuário

def atualizarReclamacoes():
    conexao = abrirBancoDados('localhost','root','password','ouvidoria')
    codigo = input("Digite o código da reclamação a ser atualizada: ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    assunto = input("Digite o assunto da reclamação: ")
    mensagem = input("Digite a mensagem da reclamação: ")
    atualizarReclamacao = 'update sistema_ouvidoria set nome = %s, email = %s, assunto = %s, mensagem = %s where codigo_reclamacao = %s'
    dados = (nome, email, assunto, mensagem, codigo)
    updateNoBancoDados(conexao, atualizarReclamacao, dados)
    encerrarBancoDados(conexao)
# Remover reclamações e dados do usuário

def removerReclamacoes():
    conexao = abrirBancoDados('localhost','root','password','ouvidoria')
    codigo = input('Digite o código da reclamação a ser removida: ')
    remover_reclamacao = 'delete from sistema_ouvidoria where codigo_reclamacao = %s'
    dados = (codigo,)
    excluirBancoDados(conexao, remover_reclamacao, dados)
    encerrarBancoDados(conexao)