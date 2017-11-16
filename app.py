# -*- coding: UTF-8 -*-
import re


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


def procurar_regex(nomes):  # Expressão regular e join
    print('Digite a expressão regular')
    regex = input()
    nomes_concatenados = ' '.join(nomes)
    resulados = re.findall(regex, nomes_concatenados)
    print(resulados)


def menu():  # Menú para escoger la opción a ejecutar
    nomes = []
    escolha = ''
    while escolha != '0':
        print('1 Para cadastrar.\n2 Para ver nomes.\n3 Para remover nomes.\n'
              '4 Para alterar nome.\n5 Para procurar un nome.\n'
              '6 Busque pela expressão regular. \n0 Para terminar.\n')
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
        elif escolha == '6':
            procurar_regex(nomes)

menu()
