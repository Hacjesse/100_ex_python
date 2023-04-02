numeros = list()
while True:
    num = int(input('Digite um valor:'))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Não pode adicionar valores iguais!')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print('-=' * 30)
print(sorted(numeros))
print('-=' * 30)




