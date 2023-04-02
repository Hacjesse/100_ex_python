from time import sleep
from pygame import mixer
for c in range(10, -1, -1):
    print(c)
    sleep(0.6)
'''mixer.init() #som de fogos, adicinal ( não faz parte do exercicio)
mixer.music.load('fogos de artificio.mp3')
mixer.music.play()
while(mixer.music.get_busy()): pass'''
print('\033[33mBUUM! BUUM!POOOOW!!!\033[m')


