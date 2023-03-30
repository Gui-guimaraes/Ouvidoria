'''
Grupo: Guilherme Guimarães, Jonathan Ferreira, Carlos Eduardo, Massimiliano Ribeiro, Gustavo Nóbrega de Carvalho, Riquelme Alves Trajano
'''

from operacoesbd import *
from sistemaOuvidoria import *

opcao = 0
reclamacoes = []

conexao = abrirBancoDados('localhost','root','Eacpncdmn3@2','ouvidoria')

while opcao != 5:
    opcao = menu()
    if opcao == 1:
        # Registrar reclamação
        reclamacaoNova = obterDados()
        print()
        print('Reclamação registrada com sucesso!')
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print()
    elif opcao == 2:
        # Listar reclamacöes
        listar = listarReclamacoes(reclamacoes)
    elif opcao == 3:
        # pesquisar reclamação por código
        print()
        pesquisar = pesquisarCodigo(reclamacoes)
        print()
    elif opcao == 4:
        # Remover reclamação
        # Autenticação do admin
        autenticado = False
        while not autenticado:
            login = input('Digite o login: ')
            senha = input('Digite a senha: ')
            autenticado = autenticar(admin, login, senha)
            if not autenticado:
                print('Usuário não autorizado')
                print()
            else:
                print()
                print('Usuário autenticado')
                print()
                # Remover reclamação
                print('listas de reclamações:')
                listar = listarReclamacoes(reclamacoes)
                remover = removerReclamacoes()
                print('Reclamação removida com sucesso!')
                print()

    elif opcao == 5:
        # Sair
        print()
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print('Até mais!')
        print()
encerrarBancoDados(conexao)