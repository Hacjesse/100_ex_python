from random import randint
computador = randint(0, 10)
print('Em que número de 0 a 10 eu pensei:')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))