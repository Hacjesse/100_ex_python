m = float(input('Digite um valor em metros: '))
mm = m*1000
cm = m*100
dm = m*10
dam = m/10
hm = m/100
km = m/1000
print('{} metros é equivalente a \n{:.0f} mm \n{:.0f} cm'.format(m, mm, cm))
print('{} dm \n{} dam \n{}hm \n{}Km'.format(dm, dam, hm, km))

