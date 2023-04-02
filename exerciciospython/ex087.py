matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if valor % 2 == 0:
            pares += valor

soma3coluna = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
print('-='*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma3coluna}.')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')