# -*- coding: UTF-8 -*-

arquivo = open('perfis.cvs', 'r')
linha = arquivo.readline()

for linha in arquivo:
    print(linha)

arquivo.close()