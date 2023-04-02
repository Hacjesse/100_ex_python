palavras = ('aprender', 'programar', 'linguagem',
            'curso', 'praticar', 'futuro',
            'mercado', 'gratis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
