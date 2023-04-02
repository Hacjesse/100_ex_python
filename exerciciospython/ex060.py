n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print('{}! é = {}'.format(n, f))

