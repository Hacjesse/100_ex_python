from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
print('O atleta tem \033[36m{}\033[m anos de idade'.format(idade))
if idade <= 9:
    print('Classificação: MIRIN')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: Master')

