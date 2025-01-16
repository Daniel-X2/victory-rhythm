import pygame
pygame.init()

caminhos=[  '/home/danields/Desktop/projeto 1/musicas/musica4.mp3',
            '/home/danields/Desktop/projeto 1/musicas/musica3.mp3',
            '/home/danields/Desktop/projeto 1/musicas/musica2.mp3',
            '/home/danields/Desktop/projeto 1/musicas/musica1.mp3']
proxima=list(caminhos.copy()) 
anterior=list()
musica_atual='kendrik.mp3'
pygame.mixer.music.load(musica_atual)
input(pygame.mixer.music.play())
pygame.mixer.music.set_volume(2)
while True:
    n1=int(input('1 ou 2'))
    if n1==1:
        try:
            if len(anterior)!=0: #and len(anterior)!=0:
                proxima.append(musica_atual)
            musica_atual=anterior.pop()
            pygame.mixer.music.load(musica_atual)
            pygame.mixer.music.play()
            
        except IndexError:
            print('sem musica')   
            print('='*50) 
            print(proxima)
            print('='*50)
            print(musica_atual)
    if n1==2:
        try:    
            if len(proxima)!=0:# and len(proxima)!=1:
                anterior.append(musica_atual)
            musica_atual=proxima.pop()    
            pygame.mixer.music.load(musica_atual)
            pygame.mixer.music.play()
            
        except IndexError:
            print('sem musica')
            print('='*50)
            print(anterior)
            print('='*50)
            print(musica_atual)








        try:
            if len(self.musica_anterior)!=0: #and len(anterior)!=0:
                self.musica_proxima.append(self.musica_atual)
            self.musica_atual=self.musica_anterior.pop()
            pygame.mixer.music.load(self.musica_atual)
            pygame.mixer.music.play()
            
        except IndexError:
            print('sem musica')   
            print('='*50) 
            print(self.musica_proxima)
            print('='*50)
            print(self.musica_atual)            