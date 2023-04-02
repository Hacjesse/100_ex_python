lista_completa = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Digite um valor: '))
    lista_completa.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else: 
        lista_impares.append(num)
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'Nn':
        break  
print('-=' * 20)
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')

