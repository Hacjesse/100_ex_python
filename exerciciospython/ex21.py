from pygame import mixer
mixer.init()
mixer.music.load('atos2.mp3')
mixer.music.play()
while(mixer.music.get_busy()): pass
# novo jeito de tocar um mp3, usando o while. na video aula de guanabara não funciona mais última linha.




