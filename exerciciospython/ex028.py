from random import randint
from time import sleep
numero = randint(0, 5) #faz o computador 'pensar'
print('-=-'*15)
print('Vou pensar em um número de 0 a 5 ')
print('-=-'*15)
adivinhe = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if numero == adivinhe:
    print('PARABÉNS! Você me venceu')
else:
    print('Ganhei!')
print('Pensei no número {}'.format(numero))



