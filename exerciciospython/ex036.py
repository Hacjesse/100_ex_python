casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário R$? '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao > minimo:
    print('EMPRÉSTIMO NEGADO, Você não pode financiar esta casa')
else:
    print('EMPRÉSTIMO ACEITO, Você pode financiar esta casa!')
