preco = float(input('Qual foi valor das compras? R$'))
print('''Selecione a forma de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção: '))
if opcao == 1:
    total = preco - (10 / 100 * preco)
    print('O valor de {:.2f} com desconto passa a ser {:.2f}.'.format(preco, total))
elif opcao == 2:
    total = preco - (5 / 100 * preco)
    print('O valor de {:.2f} passa a ser {:.2f}, com o desconto aplicado.'.format(preco, total))
elif opcao == 3:
    print('O valor a ser pago será de {:.2f}.'.format(preco))
elif opcao == 4:
    total = preco + (20 / 100 * preco)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
    print('Sua compra de {:.2f} com juros passa a ser {:.2f}.'.format(preco, total))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento, tente novamente!')