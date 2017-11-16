# -*- coding: UTF-8 -*-


def cadastrar(nomes):  # Función para ingresar nombres nuevos
    print("Digite o nome: ")
    nome = input()
    nomes.append(nome)


def listar(nomes):  # Función que lista los nombres ingresados
    print('Listando nomes: ')
    for nome in nomes:
        print(nome)


def remover(nomes):  # Función para remover un nombre
    print('O nome para remover')
    nome = input()
    nomes.remove(nome)


def alterar(nomes):  # Para modificar un nombre
    print('Qual nome vc gostaria alterar')
    nome_a_alterar = input()

    if nome_a_alterar in nomes:
        posicao =   nomes.index(nome_a_alterar)
        print('Digite novo nome')
        nome_novo = input()
        nomes[posicao] = nome_novo


def menu():  # Menú para escoger la opción a ejecutar
    nomes = []
    escolha = ''
    while escolha != '0':
        print('Digite 1 para cadastrar, 2 para ver nomes, 3 para remover nomes, 4 para alterar nombre, 0 para terminar')
        escolha = input()

        if escolha == '1':
            cadastrar(nomes)

        elif escolha == '2':
            listar(nomes)
        elif escolha == '3':
            remover(nomes)
        elif escolha == '4':
            alterar(nomes)

menu()
