peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print('O seu imc é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso ideal')
elif imc <= 25:
    print('você está no seu peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('obesidade')
else:
    print('obesidade mórbida, cuidado!')
