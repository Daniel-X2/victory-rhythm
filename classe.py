from pygame import mixer
from time import sleep
import pygame


class player():
    def __init__(self,musica):
        self.musica=musica
        
    def iniciar(musica='kendrik.mp3'):
        pygame.init()
        mixer.init()
        mixer.music.load(musica)
        mixer.music.play()
        n1=pygame.event.wait()
        
    def pausar():
        mixer.music.pause()
    def despausar():
        mixer.music.unpause()
    def reiniciar():
        mixer.music.rewind()
    def volume(volume):
        mixer.music.set_volume(volume)
    
            
player.iniciar()

