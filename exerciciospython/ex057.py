sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, digite novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))



