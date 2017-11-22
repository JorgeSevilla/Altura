# -*- coding: UTF-8 -*-

class Pessoa(object):
    'Clase para calcular IMC'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)


    def imprimir(self):
        imc = self.peso / (self.altura ** 2)
        print('O imc para: %s é %s ' % (self.nome, imc))


imc = Pessoa(nome='Jorge', peso='65', altura='1.75')
imc.imprimir()
