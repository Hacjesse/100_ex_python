from datetime import date
print('\033[31m-=-\033[m'*10)
print('ALISTAMENTO MILITAR')
print('\033[31m-=-\033[m'*10)
atual = date.today().year
print('''         DIGITE
[ 1 ] Se você for homem
[ 2 ] se você for mulher''')
opcao = int(input('Sua opção foi: '))
if opcao == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
     print('Você tem que se alistar imediatamente!')
    elif idade < 18:
     saldo = 18 - idade
     print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(18 - idade))
     ano = atual + saldo
     print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
     saldo = idade - 18
     print('Você está atrasado em {} anos para o alistamento'.format(saldo))
     ano = atual - saldo
     print(('Seu alistamento foi em {}.').format(ano))
elif opcao == 2:
    print('Você é mulher, então seu alistamento não é obrigatório!')



