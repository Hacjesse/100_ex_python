'''n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))
numeros = (n1, n2, n3, n4)
vezes9 = 0
pares = 0
print(f'Você digitou os valores: {numeros}')
for n in numeros:
    if n == 9:
        vezes9 += 1
print(f'O valor 9 apareceu {vezes9} vezes.')
for p in numeros:
    if p % 2 == 0:
        pares += 1
print(f'Os valores pares digitados foram: {pares}.')'''

num = (int(input('Didite um valor: ')), int(input('Didite um valor: ')), int(input('Didite um valor: ')), int(input('Didite um valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')




