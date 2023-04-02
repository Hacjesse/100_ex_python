from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre \033[34m{}\033[m + \033[32m{}\033[m é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação de \033[34m{}\033[m x \033[32m{}\033[m é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre os valores \033[34m{}\033[m e \033[32m{}\033[m o número {} é maior'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando!')
        sleep(2)
    else:
        print('\033[31mOpção inválida. Tente novamente\033[m')
print('Fim do programa, volte sempre!')
