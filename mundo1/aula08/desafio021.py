# Aula 08 - Programa que abre e executa um arquivo de áudio mp3

from pygame import mixer
print('========== DESAFIO 021 ==========')
mixer.init()
mixer.music.load('thief.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()
print('Reproduzindo música...')
while True:
    proxAcao = input('Digite P para parar: ')
    if proxAcao == 'P':
        mixer.music.stop()
        print('A música foi parada')
        break