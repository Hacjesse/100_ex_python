continuar = 'Ss'
cont = 0
soma = 0
maior = 0
menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média entre eles é igual a {:.1f}'.format(cont, media))
print('O maior número digitado foi o {} e o menor foi o {}'.format(maior, menor))

