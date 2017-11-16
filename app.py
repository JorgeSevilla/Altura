# -*- coding: UTF-8 -*-


def cadastrar(nomes):  # Cadastrar nomes novos
    print("Digite o nome: ")
    nome = input()
    nomes.append(nome)


def listar(nomes):  # Lista nomes cadastrados
    print('Listando nomes: ')
    for nome in nomes:
        print(nome)


def remover(nomes):  # Remover un nome
    print('O nome para remover')
    nome = input()
    nomes.remove(nome)


def alterar(nomes):  # Alterar um nome
    print('Qual nome vc gostaria alterar')
    nome_a_alterar = input()

    if nome_a_alterar in nomes:
        posicao =   nomes.index(nome_a_alterar)
        print('Digite novo nome')
        nome_novo = input()
        nomes[posicao] = nome_novo


def procurar(nomes):  # Procurar o nome cadastrado
    print('Digite nome a procurar')
    nome_a_procurar = input()
    if nome_a_procurar in nomes:
        print('Nome %s está cadastrado' % nome_a_procurar)
    else:
        print('Nome %s ñao está cadastrado' % nome_a_procurar)


def menu():  # Menú para escoger la opción a ejecutar
    nomes = []
    escolha = ''
    while escolha != '0':
        print('Digite 1 para cadastrar, 2 para ver nomes, 3 para remover nomes,'
              ' 4 para alterar nome, 5 para procurar un nome, 0 para terminar')
        escolha = input()

        if escolha == '1':
            cadastrar(nomes)
        elif escolha == '2':
            listar(nomes)
        elif escolha == '3':
            remover(nomes)
        elif escolha == '4':
            alterar(nomes)
        elif escolha == '5':
            procurar(nomes)

menu()
