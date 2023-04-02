dados = []
Tdados = []
maior = menor = 0
tot = 0
while True:
    Tdados.append(str(input('Nome: ')))
    Tdados.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = Tdados[1]
    else:
        if Tdados[1] > maior:
            maior = Tdados[1]
        if Tdados[1] < menor:
            menor = Tdados[1]
    dados.append(Tdados[:])
    Tdados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo foram cadastrados {len(dados)} pessoas') 
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end='') 
print()       
print(f'O menor peso foi de {menor}Kg. Peso de', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]')
print()

