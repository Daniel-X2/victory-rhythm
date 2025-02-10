
import os.path


class teste():
    def __init__(self,):
        self.caminhos='/home/danields/Músicas'
        self.n1=os.listdir(self.caminhos)
        self.arquivos=list()
        self.pastas=list()
        self.mp3=set()
        self.arquivo_aleatorio=list()
        self.verificador()
        self.separador()
        
        while len(self.pastas)>0:
            
            self.caminhos=self.pastas.pop()
            self.n1=os.listdir(self.caminhos)
            self.verificador()
            self.separador()
        texto=open('caminho.txt','r+')
        for c in self.mp3:
            texto.write(c+'\n')
            
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
               
                   
teste()
