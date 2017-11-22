# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrao para perfis de usuário'

    def __init__(self, nome, telefone, empresa):  # Son las carectarísticas y es un costructtor que recibe parámetros
        if(len(nome) < 3):
            raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.curtidas = 0
        #self.__tipo = tipo

    def imprimi(self):
        print('Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    #  @staticmethod   # Decorator Método de clase
    @classmethod  # para código genérico recibe como parámetro el nombre de clase
    def gerar_perfil(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise ValueError('Uma linha no arquivo % s deve ter 3 valores' % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis


class Perfil_Vip(Perfil):
    'Classe padrao para perfis de usuário'

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)  # Super Para ingresar clase padre de clase hija
        self.apelido = apelido

    def obter_creditos(self):
        if self.__tipo == 0:
            return super(Perfil_Vip, self).obter_curtidas() * 10  # Se usa super para ingresar a la clase padre

class ArgumentoInvalidoError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return repr(self.mensagem)

# perfil = Perfil(nome='Jorge Sevilla', telefone='991502621', empresa='X')
# perfil2 = Perfil(empresa='x', nome='Jorge Sevilla', telefone='1234')
# perfil2.imprimi()
# perfil.curtir()
# perfil.curtidas