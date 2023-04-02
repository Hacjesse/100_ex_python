n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {} sua média é {}'.format(n1, n2, media))
if media >= 7 and media <= 10:
    print('APROVADO')
elif 5 <= media <= 6.9:
    print('Recuperação')
elif media < 5:
    print('REPROVADO')
else:
    print('Nota(s) inválida(s)')


