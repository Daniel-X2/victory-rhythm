import PIL.Image 
import customtkinter as ctk 
import customtkinter 
import PIL 
from PIL import Image,ImageTk 
from capas import backgroud
from pygame import mixer
import pygame
from capas import titulo
from time import sleep
from customtkinter import filedialog
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        mixer.init()
        self.proximo=list()
        self.musica_atual='kendrik.mp3'
    #acho necessario um verificador pra os arquivos no diretorio
        self.geometry('400x600')
        self.resizable(width=False,height=False)   #aqui evita que a tela seja redimesionada
        self.capa_musica()
        self.botao()
        #self.update_barra()
        self.n1=1
        self.sei()
        self.player('kendrik.mp3')
        self.musicas_anterior=list()
        self.update_total()
        self.update_label()
        self.musicas=list()
        self.botao_play()
    def player(self,musica):
        mixer.init()
        mixer.music.load(musica)
        mixer.music.play()
        
    def pausar(self):
        mixer.music.pause()
    def despausar(self):
        mixer.music.unpause()    
    def capa_musica(self,):    
        back=backgroud.capa(self.musica_atual)
        if back==0:
            capa_musica= customtkinter.CTkImage(Image.open('capa_padrao.jpeg'), size=(300,300))
        else:
            capa_musica= customtkinter.CTkImage(Image.open('imagem.jpg'), size=(300,300))
        self.capa=ctk.CTkLabel(master=self,image=capa_musica,text='',width=10,height=10,anchor='center')
        self.capa.place(x=45,y=50) 
    def botao(self):
        #botao anterior
        botao_a = customtkinter.CTkImage(Image.open("anterior.png"), size=(41, 28))
        botao_anterior=ctk.CTkButton(self,image=botao_a,width=10,height=10,text='',fg_color='#242424',bg_color='#242424')
        botao_anterior.place(x=114,y=470)
        #botao proximo
        botao_p = customtkinter.CTkImage(Image.open("proximo.png"), size=(41,28))
        botao_proximo=ctk.CTkButton(self,text='',image=botao_p,width=10,height=10,fg_color='#242424',bg_color='#242424')
        botao_proximo.place(x=231,y=470)       
    def update_barra(self):
        #infomaçoes da barra
        progresso=customtkinter.IntVar()
        duraçao=titulo.info()[0]
        barra=customtkinter.CTkSlider(self,from_=0,to=duraçao,width=360,variable=progresso,border_color='#242424',)
        #mixer.music.set_pos(progresso.get())
        barra.place(x=20,y=440)
        #atualizaçao do progresso
        barra.after(1000,self.update_barra) # chama este método novamente em 1.000 milissegundos
    def botao_play(self):
        n1=self.n1
        global button_image
        global image_button
        if n1%2==0:
            self.pausar()
            button_image = customtkinter.CTkImage(Image.open("play1.png"), size=(30, 30)) 
            image_button = customtkinter.CTkButton(master=self,anchor='center',image=button_image,width=10,height=10,corner_radius=50,text='',fg_color='#242424',command=self.botao_play)
            self.n1+=1
            image_button.place(x=182,y=470)
        else:
            self.despausar()
            button_image = customtkinter.CTkImage(Image.open("pause.png"), size=(32, 32)) 
            image_button = customtkinter.CTkButton(master=self,anchor='center',text="",image=button_image,width=10,height=10,corner_radius=50,fg_color='#242424',command=self.botao_play)
            self.n1+=1
            image_button.place(x=182,y=470)
    def sei(self):
        milisegundos=0
        self.segundos=0
        hora=0
        minutos=0    
        #contador label
        self.texto=ctk.CTkLabel(self,text='')
        self.texto.place(x=50,y=450)
        #duraçao=titulo.info()[0]
        #autor=titulo.info()[1]
        #duraçao atual da musica
    def update_label(self,segundos=0,minutos=0,hora=0):
        musica_label=self.musica_atual
        if musica_label!=self.musica_atual:
            self.update_label()
        if mixer.music.get_busy():
            self.segundos+=1
        else:
            pass
        segundos=self.segundos
        #if True:
        #if mixer.music.get_busy():
            #segundos+=1
        #else:
            #pass
        if segundos==60:
            segundos=0
            minutos+=1
        elif segundos>60:
            while segundos>60:
                segundos-=60
                minutos+=1 
        if segundos<10 and minutos<10:
            self.texto.configure(text = f'0{hora}:0{minutos}:0{segundos}')
        elif segundos<10 and minutos>=10:
            self.texto.configure(text = f'0{hora}:{minutos}:0{segundos}')
        elif segundos>=10 and minutos<10:
            self.texto.configure(text = f'0{hora}:0{minutos}:{segundos}')
        elif segundos>=10 and minutos>=10:
            self.texto.configure(text = f'0{hora}:{minutos}:{segundos}')
        
        self.texto.after(1000,self.update_label) # chama este método novamente em 1.000 milissegundos    
    def update_total(self):
        #duraçao total da musica
        
        self.duraçao=titulo.info(musica=self.musica_atual)[0]
        
        segundos_total=self.duraçao
        minutos_total=0
        horas_total=0
        self.total=ctk.CTkLabel(self,text='')
        self.total.place(x=300,y=450)
        if segundos_total==60:
            segundos_total=0
            minutos_total+=1
        elif segundos_total>60:
            while segundos_total>60:
                segundos_total-=60
                minutos_total+=1 
        if segundos_total<10 and minutos_total<10:
            self.total.configure(text = f'0{horas_total}:0{minutos_total}:0{segundos_total}')
        elif segundos_total<10 and minutos_total>=10:
            self.total.configure(text = f'0{horas_total}:{minutos_total}:0{segundos_total}')
        elif segundos_total>=10 and minutos_total<10:
            self.total.configure(text = f'0{horas_total}:0{minutos_total}:{segundos_total}')
        elif segundos_total>=10 and minutos_total>=10:
            self.total.configure(text = f'0{horas_total}:{minutos_total}:{segundos_total}')
    def pastas(self):
        
        try:
            #aqui vai escrever o caminho da pasta que o usuario vai escolher
            caminhos_musica=open('caminhos.txt','+a')
            self.abrir_diretorio=filedialog.askdirectory('abra a pasta de suas musicas')
            n3=self.n1[0]
            caminhos_musica.writelines(n3)
            caminhos_musica.close()
            #aqui vai abrir o mesmo aquivo de texto mas mode leitura
            caminhos_musica=open('caminhos.txt','+rb')
            n1=set(caminhos_musica.readlines())# aqui vai evitar ter musica repetida
            caminhos_musica=open('caminhos.txt','w+')
            caminhos_musica.close()
            caminhos_musica=open('caminhos.txt','+a')    
            n3=0
            for c in n1:
                n3=bytes.decode(c)
                caminhos_musica.write(n3)
                caminhos_musica.close()   
        except:
            #aqui vai criar o arquivo caminhos.txt 
            caminhos_musica=open('caminhos.txt','w+')
            self.abrir_diretorio=filedialog.askdirectory('abra a pasta de suas musicas')
            n3=self.n1[0]
            caminhos_musica.writelines(n3)
            caminhos_musica.close()
            #aqui vai abrir o mesmo aquivo de texto mas mode leitura
            caminhos_musica=open('caminhos.txt','+rb')
            n1=set(caminhos_musica.readlines())# aqui vai evitar ter musica repetida
            caminhos_musica=open('caminhos.txt','w+')
            caminhos_musica.close()
            caminhos_musica=open('caminhos.txt','+a')    
            n3=0
            for c in n1:
                n3=bytes.decode(c)
                caminhos_musica.write(n3)
                caminhos_musica.close()   
    def tirar_musica(self):
        mixer.music.unload()   
    def reiniciar_musica():
        mixer.music.rewind()    
    def caminhos(self):
        try:
            caminhos=open('caminhos.txt','r+')
        except FileNotFoundError:
            caminhos=open('caminhos.txt','w+')
            #aqui tenho que colocar o negocio de abrir o diretorio
        for c in caminhos.read():
            
app=App()
app.mainloop()

#objetivo 1: tenho que ajeitar a questao de proximas musicas e musicas anterior
#2: dar a opçao de baixar as capas onlline 
#3 deixar automatico a mudança do titulo e das ccapas
#4 colocar volume
#5 deixar funcional a barra de progresso
#6 colocar um negocio de sobre o projeto 
#7 colocar opçao de preferencias 

