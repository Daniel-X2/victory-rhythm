import pygame
pygame.init()

caminhos=['/home/daniel/Área de trabalho/projeto 1/musicas/001.KORDHELL - MURDER IN MY MIND.mp3',
'/home/daniel/Área de trabalho/projeto 1/musicas/01.LXNGVX - YUM YUM (Super Slowed ｜ TikTok Edition).mp3',
'/home/daniel/Área de trabalho/projeto 1/musicas/04.DJ OLIVER MENDES - BRUTAL INFERNAL FUNK (OFFICIAL VIDEO).mp3',
'/home/daniel/Área de trabalho/projeto 1/musicas/004.DVRST - Close Eyes.mp3',]
proxima=list(caminhos.copy())
anterior=list()
musica_atual='kendrik.mp3'

pygame.mixer.music.load(musica_atual)
input(pygame.mixer.music.play())
while True:
    n1=int(input('1 ou 2'))
    if n1==1:
        try:
            print(musica_atual)
            proxima.append(musica_atual)
            musica_atual=anterior.pop()
            pygame.mixer.music.load(musica_atual)
            pygame.mixer.music.play()
        except IndexError:
            print('sem musica')    
    if n1==2:
        try:    
            print(musica_atual)
            anterior.append(musica_atual)
            musica_atual=proxima.pop()
            pygame.mixer.music.load(musica_atual)
            pygame.mixer.music.play()
        except IndexError:
            print('sem musica')