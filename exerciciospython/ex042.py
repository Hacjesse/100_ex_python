seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    if seg1 == seg2 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo equilátero!')
    elif seg1 == seg2 or seg1 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo isósceles!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo escaleno!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')

