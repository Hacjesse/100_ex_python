print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
amais = 10
while amais != 0:
    total += amais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    amais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com \033[30m{}\033[m termos!'.format(total))
