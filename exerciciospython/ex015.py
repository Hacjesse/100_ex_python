dias = int(input('Quantos dias alugados? '))
km = float(input('Qual a quantidade de km percorridos? '))
preço = (60 * dias) + (0.15 * km)
print('O total a pagar é R${:.2f}'.format(preço))


