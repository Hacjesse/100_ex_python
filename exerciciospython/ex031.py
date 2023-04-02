distancia = float(input('Qual a distancia a ser percorrida em Km/h? '))
print('Você está prestes a começar uma jornada de {}Km'.format(distancia))
if distancia <= 200:
    taxa1 = 0.5 * distancia
    print(('O valor da viagem será de R${:.2f}').format(taxa1))
else:
    taxa2 = 0.45 * distancia
    print('O valor da viagem será de R${:.2f}'.format(taxa2))
