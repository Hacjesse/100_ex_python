from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
print('O seno de {:.2f} é igual a {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O cosseno de {:.2f} é igual a {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('A tangente de {:.2f} é igual a {:.2f}'.format(an, tan))


