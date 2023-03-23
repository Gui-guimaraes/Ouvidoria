from operacoesbd import *
from sistemaOuvidoria import *

opcao = 0
reclamacoes = []

conexao = abrirBancoDados('localhost','root','password','ouvidoria')

while opcao != 5:
    print('Ola! seja bem-vindo a ouvidoria')
    print('1 - Registrar reclamação')
    print('2 - Listar reclamações')
    print('3 - Pesquisar reclamação por código')
    print('4 - Remover reclamação')
    print('5 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        # Registrar reclamação
        reclamacaoNova = obterDados()
        print()
        print('Reclamação registrada com sucesso!')
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print()
    elif opcao == 2:
        # Listar reclamacöes
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
                print('Email: ', reclamacao[2])
                print('Assunto: ', reclamacao[3])
                print('Mensagem: ', reclamacao[4])
                print()
    elif opcao == 3:
        # pesquisar reclamação por código
        print()
        print('Pesquisar reclamação por código')
        codigo = (input('Digite o código da reclamação a ser pesquisado: '))
        consultarListagem = 'select * from sistema_ouvidoria where codigo_reclamacao = ' + codigo
        listaReclamacao = listarBancoDados(conexao, consultarListagem)

        if len(listaReclamacao) == 0:
            print('Não há reclamações registradas')
        else:
            print()
            print('Listando reclamações...')
            for reclamacao in listaReclamacao:
                print('Código: ', reclamacao[0])
                print('Nome: ', reclamacao[1])
                print('Email: ', reclamacao[2])
                print('Assunto: ', reclamacao[3])
                print('Mensagem: ', reclamacao[4])
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
                listar = listarReclamacoes()
                remover = removerReclamacoes()
                print('Reclamação removida com sucesso!')

    elif opcao == 5:
        # Sair
        print()
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print('Até mais!')
        print()
encerrarBancoDados(conexao)