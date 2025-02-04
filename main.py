import customtkinter as ctk 
import customtkinter 
from PIL import Image,ImageTk
from capas import backgroud
from pygame import mixer
import pygame
from capas import titulo
from time import sleep
from customtkinter import filedialog
import tkinter
class musica_window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("550x350")
        self.config(background='#242424')
        self.resizable(width=False,height=False)
        self.title('musicas')
    def teste(self):
        n1=open('caminho.txt','r')
        for c in n1.read():
            
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("550x350")
        self.config(background='#242424')
        self.resizable(width=False,height=False)
        self.tabview()
        self.title('configuraçao')
    def tabview(self):
        tabview = customtkinter.CTkTabview(master=self,
                                            anchor='nw',
                                            fg_color='#242424',
                                            width=500,height=330,
                                            border_width=2,
                                            border_color='gray',
                                            segmented_button_selected_color='#242424',
                                            bg_color='#242424',
                                            segmented_button_fg_color='#242424',
                                            #segmented_button_unselected_color='black',
                                            segmented_button_unselected_hover_color='black',#cor de quando passa o mouse
                                            corner_radius=10)
        tabview.place(x=25,y=10)
        tabview.add("geral")  # add tab at the end
        tabview.add("sobre")  # add tab at the end
        tabview.set("geral")  # set currently visible tab

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        optionmenu = customtkinter.CTkOptionMenu(master=tabview.tab('geral'), values=["option 1", "option 2"],
                                         command=optionmenu_callback)
        optionmenu.set("option 2")
        optionmenu.place(x=10,y=10)


        

        frame1=customtkinter.CTkFrame(master=tabview.tab('geral'),corner_radius=15,width=200,height=200,border_color='black',border_width=2,fg_color='#242424')
        #frame1.place(x=10,y=20)
        frame2=customtkinter.CTkFrame(master=tabview.tab('geral'),corner_radius=15,width=200,height=200,border_color='black',border_width=2,fg_color='#242424')
        #frame2.place(x=270,y=20)


        switch_var = customtkinter.StringVar(value="on")
        switch = customtkinter.CTkSwitch(master=tabview.tab('geral'), text="capas online",
                                variable=switch_var, onvalue="on", offvalue="off",bg_color='black')
        #switch.place(x=10,y=40)


        self.textbox = customtkinter.CTkTextbox(master=tabview.tab('sobre'), width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)
        #tab_1 = tabview.add("tab 3")
        #tab_2 = tabview.add("tab 4")

        #button = customtkinter.CTkButton(tab_1)
class App(customtkinter.CTk):
    def __init__(self):

        super().__init__()
        mixer.init()
        mixer.music.set_volume(0)
        self.geometry('400x600')
        self.config(background='#242424')
        self.title('player')
        self.resizable(width=False,height=False)   #aqui evita que a tela seja redimesionada
        self.variaveis_funçoes()
        self.funçoes_iniciais()
        self.subtitulo()
        

        
    def funçoes_iniciais(self):
        self.botao() 
        self.label()
        self.backgroud()
        self.variavel_do_total()
        self.update_total()
        self.update_barra()
        self.update_label()
        self.botao_play()
        self.player(self.musica_atual)
        self.botao_janela()
    def variaveis_funçoes(self):
        self.segundos=self.minutos=self.hora=0
        self.image_button=customtkinter.CTkButton(master=self,text='')
        self.image_button.place(x=182,y=470)
        self.musica_atual='kendrik.mp3'
        self.progresso=customtkinter.DoubleVar()
        self.vari=0
        self.n1=1#aqui ativa o botao play
        self.caminhos=[ 'kendrik.mp3','/home/danields/Desktop/projetos/player_musica/musicas/musica1.mp3']
        self.musica_anterior=list()
        self.musica_proxima=list(self.caminhos.copy())
        self.titulo_atual=titulo.info(self.musica_atual)[1]
        self.title(self.titulo_atual)
    def backgroud(self):
        self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300)) 
        self.imagem_fundo=customtkinter.CTkLabel(self,text='',image=self.back)
        self.imagem_fundo.place(x=50,y=50)
    def player(self,musica):#tudo ok por aqui
        mixer.init()
        mixer.music.load(musica)
        mixer.music.play()    
    def pausar(self):#tudo ok por aqui
        mixer.music.pause()
    def despausar(self):#tudo ok por aqui
        mixer.music.unpause()    
    def botao(self):#tudo ok por aqui
        #botao anterior
        botao_a = customtkinter.CTkImage(Image.open("/home/danields/Desktop/projetos/player_musica/imagens/anterior.png"),
                                                    size=(41, 28))
        botao_anterior=ctk.CTkButton(self,image=botao_a,
                                    width=10,
                                    height=10,
                                    text='',
                                    fg_color='#242424',
                                    bg_color='#242424',
                                    command=self.anterior)
        botao_anterior.place(x=114,y=470)
        #botao proximo
        botao_p = customtkinter.CTkImage(Image.open("/home/danields/Desktop/projetos/player_musica/imagens/proximo.png"),
                                                    size=(41,28))
        botao_proximo=ctk.CTkButton(self,text='',
                                    image=botao_p,
                                    width=10,
                                    height=10,
                                    fg_color='#242424',
                                    bg_color='#242424',
                                    command=self.proximo)
        botao_proximo.place(x=231,y=470)       
    def botao_play(self):# aqui esta ok 
        n1=self.n1
        
        self.image_button.destroy()
        if n1%2==0:
            self.pausar()
            self.button_image = customtkinter.CTkImage(Image.open("/home/danields/Desktop/projetos/player_musica/imagens/play1.png"), size=(30, 30)) 
            self.image_button = customtkinter.CTkButton(master=self,
                                                anchor='center',
                                                image=self.button_image,
                                                width=10,
                                                height=10,
                                                text='',
                                                fg_color='#242424',
                                                command=self.botao_play,
                                                bg_color='#242424')
            
            self.n1+=1
            
            self.image_button.place(x=182,y=470)
            
        else:
            self.despausar()
            self.button_image = customtkinter.CTkImage(Image.open("/home/danields/Desktop/projetos/player_musica/imagens/pause.png"), size=(32, 32))
            self.image_button = customtkinter.CTkButton(master=self,
                                                anchor='center',
                                                text="",
                                                image=self.button_image,
                                                width=10,
                                                height=10,
                                                corner_radius=50,
                                                bg_color='#242424',
                                                command=self.botao_play)
            
            
            self.n1+=1

            self.image_button.place(x=182,y=470)      
    def label(self):# aqui esta tudo ok
        self.texto=ctk.CTkLabel(self,text='',bg_color='#242424',text_color='black')
        self.texto.place(x=50,y=450)
    def update_label(self,segundos=0,hora=0,minutos=0):#aqui esta tudo ok
        if mixer.music.get_busy():
            self.segundos+=1
            self.vari=self.progresso.get()
            self.vari+=1
            self.progresso.set(self.vari)
            print(self.vari,self.segundos)
        else:
            pass
        
        if self.segundos==60:
            self.segundos=0
            self.minutos+=1
        elif self.segundos>60:
            while self.segundos>60:
                self.segundos-=60
                self.minutos+=1 
        if self.segundos<10 and minutos<10:
            self.texto.configure(text = f'0{self.hora}:0{self.minutos}:0{self.segundos}\r')
        elif self.segundos<10 and self.minutos>=10:
            self.texto.configure(text = f'0{self.hora}:{self.minutos}:0{self.segundos}')
        elif self.segundos>=10 and self.minutos<10:
            self.texto.configure(text = f'0{self.hora}:0{self.minutos}:{self.segundos}')
        elif self.segundos>=10 and self.minutos>=10:
            self.texto.configure(text = f'0{self.hora}:{self.minutos}:{self.segundos}')
        
        
        self.texto.after(1000,self.update_label) # chama este método novamente em 1.000 milissegundos  
    def variavel_do_total(self):
        self.total=ctk.CTkLabel(self,text='',bg_color='#242424',text_color='black')
        self.total.place(x=300,y=450)
    def update_total(self):#aqui esta tudo ok
        #duraçao total da musica
        self.duraçao=titulo.info(musica=self.musica_atual)[0]
        segundos_total=self.duraçao
        minutos_total=0
        horas_total=0
        
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
        #self.total.after(1000,self.update_total)    
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
    def tirar_musica(self):#tudo ok por aqui
        mixer.music.unload()   
    def reiniciar_musica():#tudo ok por aqui
        mixer.music.rewind()    
    def proximo(self):#tudo ok por aqui
        try:
            self.tirar_musica() 
            if len(self.musica_proxima)!=0:# and len(proxima)!=1:
                self.musica_anterior.append(self.musica_atual)
                
            self.musica_atual=self.musica_proxima.pop()    
            pygame.mixer.music.load(self.musica_atual)
            pygame.mixer.music.play()
            if self.n1%2==0:
                pass
            else:
                self.botao_play()
            self.update_total()
            #aqui serve pra atualizar a capa das musicas
            self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300)) 
            self.imagem_fundo=customtkinter.CTkLabel(self,text='',image=self.back)
            self.imagem_fundo.place_configure(x=50,y=50)

            #aqui reseta os segundos e os minutos do update label
            self.segundos=self.minutos=0
            #atualiza o titulo da janela
            self.titulo_atual=titulo.info(self.musica_atual)[1]
            self.title(self.titulo_atual)
            #aqui atualiza a duraçao da barra 
            self.duraçao=titulo.info(musica=self.musica_atual)[0]
            self.progresso.set(0)
            self.barra.configure(variable=self.progresso,to=self.duraçao)
            

            self.autor=titulo.info(self.musica_atual)[2]
            self.sub_titulo.configure(text=self.autor)
        except IndexError:
            print('sem musica')
            print('='*50)
            print(self.musica_anterior)
            print('='*50)
            print(self.musica_atual)        
    def anterior(self):
        try:
            if len(self.musica_anterior)!=0: #and len(anterior)!=0:
                self.musica_proxima.append(self.musica_atual)
            self.musica_atual=self.musica_anterior.pop()
            pygame.mixer.music.load(self.musica_atual)
            pygame.mixer.music.play()
            if self.n1%2==0:
                pass
            else:
                self.botao_play()  
            self.update_total()    

            #pega a nova capa e coloca
            self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300)) 
            self.imagem_fundo=customtkinter.CTkLabel(self,text='',image=self.back)
            self.imagem_fundo.place_configure(x=50,y=50)
            #reseta os segundos 
            self.segundos=self.minutos=self.hora=0
            #atualiza o titulo da janela
            self.titulo_atual=titulo.info(self.musica_atual)[1]
            self.title(self.titulo_atual)
            #aqui atualiza a duraçao da barra
            self.duraçao=titulo.info(musica=self.musica_atual)[0]
            self.progresso.set(0)
            self.barra.configure(to=self.duraçao,variable=self.progresso)


            self.autor=titulo.info(self.musica_atual)[2]
            self.sub_titulo.configure(text=self.autor)
        except IndexError:
            print('sem musica')   
            print('='*50) 
            print(self.musica_proxima)
            print('='*50)
            print(self.musica_atual)  
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    def botao_janela(self):  
        #imagem=customtkinter.CTkImage(Image.open('/home/danields/Desktop/projetos/player_musica/imagens/ponto.png'), size=(30,30))
        #self.button_1 = customtkinter.CTkButton(self, text="", command=self.open_toplevel,width=15,height=15,image=imagem,fg_color='#242424',bg_color='#242424')
        #self.button_1.place( x=360, y=10)
        self.musica_window= None
        self.toplevel_window = None 
        def optionmenu_callback(opcoes):
            if opcoes=='Opçoes':
                pass
            elif opcoes=='Musicas':
                self.musicas()
            else:
                self.open_toplevel()   
        optionmenu = customtkinter.CTkOptionMenu(master=self, values=["Opçoes","Musicas","Geral"],width=50,
                                            command=optionmenu_callback,)
        optionmenu.set("opçoes")
        optionmenu.place(x=320,y=10)

    def musicas(self):
        if self.musica_window is None or not self.musica_window.winfo_exists():
            self.musica_window = musica_window(self)  # create window if its None or destroyed
        else:
            self.musica_window.focus()  # if window exists focus it
    def update_barra(self):# aqui falta fazer funcionar de forma normal
        #infomaçoes da barra
        self.vari=self.progresso.get()
        #print(self.progresso.get())
        self.vari+=1
        self.progresso.set(self.vari)
        print(self.vari)
        
        self.barra=customtkinter.CTkSlider(self,from_=0,
                                    to=self.duraçao,
                                    width=360,
                                    variable=self.progresso,
                                    border_color='#242424',
                                    bg_color='#242424'
                                    ,command=lambda n1:self.progresso_atual())#,(mixer.music.set_pos(self.progresso.get()))))#aqui tentar if simples pra resolver o b.o 
        self.barra.place(x=20,y=430)
    def progresso_atual(self):
        self.progresso.set(self.progresso.get())
        if mixer.music.get_busy():
            mixer.music.set_pos(self.progresso.get())
    def subtitulo(self):
        self.autor=titulo.info(self.musica_atual)[2]
        self.sub_titulo=customtkinter.CTkLabel(self,text=self.autor)
        self.sub_titulo.place(x=140,y=400)
app=App()
app.mainloop()


#2: dar a opçao de baixar as capas onlline 
#3 deixar automatico a mudança do titulo e das ccapas
#4 colocar volume
#5 deixar funcional a barra de progresso
#6 colocar um negocio de sobre o projeto 
#7 colocar opçao de preferencias 

