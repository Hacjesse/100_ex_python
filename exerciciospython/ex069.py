maiorque18 = homem = mulhermenos20 = 0
while True:
    print('-=-'*10)
    print('CADASTRE UMA PESSOA')
    print('-=-'*10)
    idade = int(input('Idade: '))
    if idade > 18:
        maiorque18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo in 'Mm':
        homem += 1
    print('-=-'*10)
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer Continuar? [S/N] ').upper()[0]
    if continuar in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {maiorque18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulhermenos20} mulheres com menos de 20 anos.')
