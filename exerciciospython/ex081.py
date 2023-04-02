numeros = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    cont += 1
    r = str(input('Quer continuar? [S/N]')).upper()  
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
print('-=' * 30)
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print('-=' * 30)
if 5 in numeros:
    print('O valor 5 está na lista!')
    print('-=' * 30)
else:
    print('O valor 5 não foi encontrado na lista!')
    print('-=' * 30)

        


