import os.path
import pygame
class teste():
    def __init__(self,):
        self.caminhos='/home/danields/Músicas/oi'
        self.n1=os.listdir(self.caminhos)
        self.arquivos=list()
        self.pastas=list()
        self.mp3=set()
        self.verificador()
        self.separador()
        
        while len(self.pastas)>0:
            
            self.caminhos=self.pastas.pop()
            self.n1=os.listdir(self.caminhos)
            self.verificador()
            self.separador()
        caminho=open('caminho.txt','r+')
        for c in self.mp3:
            caminho.write(c+'\n')
        caminho.close()    
        self.impedir_duplicatas() 
        print('acabou')    
    def verificador(self):
        for c in self.n1:
            junçao=self.caminhos+'/'+c
            if os.path.isfile(junçao):
                self.arquivos.append(junçao)
            elif os.path.isdir(junçao):
                self.pastas.append(junçao)
    def separador(self):
        for c in self.arquivos:
            if '.mp3' in c :
                self.mp3.add(c)
    def impedir_duplicatas(self):
        try:
            caminho=open('caminho.txt','r+')
        except FileNotFoundError:
            caminho=open('caminho.txt','w+')
        try:
            open_dupli=open('duplicata.txt','r+')
        except FileNotFoundError:
            open_dupli=open('duplicata.txt','w+')
        duplicata=set()
        caminho.close()
        caminho=open('caminho.txt','r+')
        for c in caminho.readlines():
            #print(c)
            if c=='\n':
                pass
            elif '\n' in c:
                duplicata.add(c)
            else:
                c=c+'\n'
                duplicata.add(c)
        
        for c in duplicata:
            open_dupli.writelines(c)
        caminho.close()
        open_dupli.close()        
    def sobrescrever(self):
        caminho=open('caminho.txt','w+')  
        open_dupli=open('duplicata.txt','r+')
        for c in open_dupli:
            caminho.writelines(c)
pygame.mixer.init()
pygame.mixer.music.load('kendrik.mp3')
input(pygame.mixer.music.play())
pygame.mixer.music.set_endevent(5)
print(pygame.mixer.music.get_endevent())
