lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = (lar*alt)
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lar, alt, area))
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))
