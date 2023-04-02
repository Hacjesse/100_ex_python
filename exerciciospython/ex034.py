salario = float(input('Qual o seu salário? '))
if salario > 1250:
    novo = salario + (10 / 100 * salario)
else:
    novo = salario + (15 / 100 * salario)
print('O seu salario antigo era de {:.2f} e agora passa a ganhar {:.2f}R$'.format(salario, novo))



