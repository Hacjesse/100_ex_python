preço = float(input('Qual o preço do produto? R$'))
desc = preço - (preço * 0.05)
print('O preço do produto custava {:.2f}, e com o desconto de 5% vai custar R${:.2f}'.format(preço, desc))

