print('\033[31m-=-\033[m'*10)
print('\033[34mANALIZADOR DE TRIANGULOS\033[m')
print('\033[31m-=-\033[m'*10)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')

