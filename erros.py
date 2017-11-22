# import models
from models import *
arquivo = None
try:
    with open('perfis.cvs', 'r')as arquivo
        for linha in arquivo:
            print(linha)
#     open('perfis.cvs', 'r')
#     valores = arquivo.readline().split(':')
#     Perfil(*valores)
#     print('arqiuvo abierto')
#     arquivo.close
# except (IOError, TypeError) as error:
#     print('Deu IOerror % s' % error)
# finally:
#     if(arquivo != not None):
#         print('fechando arquivo')
#         arquivo.close()