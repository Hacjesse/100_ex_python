vel = float(input('Qual a sua velocidade em Km/h? '))
if vel > 80:
    print(('MULTADO! Você excedeu o limite de 80 Km/h'))
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
