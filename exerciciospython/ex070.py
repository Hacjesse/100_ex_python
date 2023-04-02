soma = maisde1000 = menor = cont = 0
prodbarato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        prodbarato = produto
    if preço > 1000:
        maisde1000 += 1
    soma += preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi: {soma:.2f}')
print(f'Teve {maisde1000} produtos que custaram mais de R$1000.00')
print(f'o produto mais barato foi {prodbarato} que custou R&{menor:.2f}')

