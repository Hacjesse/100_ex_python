from random import randint
cont = 0
while True:
    comp = randint(0, 10)
    num = int(input('Diga um valor: '))
    poi = str(input('[P/I]? ')).upper()
    soma = num + comp
    if poi == 'P' and soma % 2 == 0:
        print(f'Você jogou {num} e o computador {comp}. total de {soma} deu PAR')
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente')
        cont += 1
    if poi == 'I' and soma % 2 != 0:
        print(f'Você jogou {num} e o computador {comp}. total de {soma} deu IMPAR')
        print('VOCÊ VENCEU')
        cont += 1
        print('Vamos jogar novamente')
    if poi == 'P' and soma % 2 != 0:
        print(f'Você jogou {num} e o computador {comp}. total de {soma} deu IMPAR')
        print('VOCÊ PERDEU')
        break
    if poi == 'I' and soma % 2 == 0:
        print(f'Você jogou {num} e o computador {comp}. total de {soma} deu PAR')
        print('VOCÊ PERDEU')
        break
print(f'GAME OVER! Você venceu {cont} vezes')
