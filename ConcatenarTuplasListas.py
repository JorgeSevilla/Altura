status_civil = ('casado', 'solteiro') + ('divorciado',)
tipo = type(status_civil)
estados = ('RJ', 'SP') + tuple(['MG', 'ES'])  # Convierte a tulpa
tipo2 = type(estados)
print (status_civil, tipo)
print(estados, tipo2)  # Se imprime la tupla contatenada