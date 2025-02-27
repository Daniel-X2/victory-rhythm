import os.path
import customtkinter as ctk 
import customtkinter 
from PIL import Image,ImageTk
from capas import titulo
from pygame import mixer
import pygame
from customtkinter import filedialog
import tkinter
from sqlalchemy import Column, Integer, String,ForeignKey,Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#aqui cria o banco de dados ou utiliza se ja existe
engine = create_engine('sqlite:///:meu.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class Caminho(Base):
    __tablename__ = 'caminho'  # if you use base it is obligatory

    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    diretorio = Column(String)
    #status=Column(Boolean)

Base.metadata.create_all(engine)
atualizador=''
musicas=0
n1=0
#falta fazer a musica ir automaticamente pra a proxima musica

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):# falta colocar um verificador pra nao colocar musicas que nao funcionanm aqui
        super().__init__(master, **kwargs)
        global dici,session
        self.session=session
        # add widgets onto the frame...
        mixer.init()
        self.label = customtkinter.CTkLabel(self,text='',height=69)
        self.label.grid(row=0, column=0, padx=20)
        self.n4=0
        
        
        #aqui vai fazer um requerimento e pegar os diretorios e os nomes das musicas
        self.diretorio=session.query(Caminho.diretorio).all()
        self.nome_musica=session.query(Caminho.name).all()
        self.dici=dict()
        self.n2=list()
        self.n3=list()
        for c in self.nome_musica:
            for n in c:
                self.n2.append(n)
        self.n3=self.n2.copy()
        for c in self.diretorio:
            for n in c:
                self.dici[self.n2.pop(0)]=n
        #esse tamanho vai ser usado pra ver a quantidade das musicas e colocar na janela        
        tamanho=27*(len(self.n3))
        self.label.configure(height=tamanho)
    
        if len(self.n3)>0:
            while len(self.n3)>0:
                self.criar()          
    def criar(self):#aqui cria os botoes de forma automatica
        global atualizador
        try:
            
            nome_musica=self.n3.pop()
            if nome_musica=='r':
                self.criar()
            else:    
                try:
                    #mixer.music.load(self.dici[nome_musica])
                    self.n1=customtkinter.CTkButton(self,text=nome_musica,width=400,command=lambda:self.player_botao(dici=self.dici,nome_musica=nome_musica))#(mixer.music.unload(),mixer.music.load(self.dici[nome_musica]),(mixer.music.play()),(self.atualizador(self.dici[nome_musica]))))
                    self.n1.place(x=-5,y=self.n4)
                    self.n4+=27
                except:
                    self.criar()
            
        except:
            return
    def atualizador(self,dici):#aqui e um atualizador entre classes
        global atualizador
        atualizador=dici
    def player_botao(self,dici,nome_musica):
        try:
            mixer.music.unload()
            mixer.music.load(dici[nome_musica])
            mixer.music.play()
            self.atualizador(dici[nome_musica])
        except:#se der erro ira excluir do banco de dados a musica que deu erro
            usu=self.session.query(Caminho).filter_by(name=nome_musica).first()
            usu2=self.session.query(Caminho).filter_by(diretorio=dici[nome_musica]).first()
            self.session.delete(usu)
            self.session.delete(usu2)
            self.session.commit()
            self.n1.destroy()
            
class musica_window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self, width=410, height=200, corner_radius=0,fg_color='#242424')
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        self.geometry("400x400")
        self.resizable(width=False,height=False)
        self.config(background='#242424') 
        self.title('Musicas')
   
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
                                            
                                            segmented_button_unselected_hover_color='black',#cor de quando passa o mouse
                                            corner_radius=10)
        tabview.place(x=25,y=10)
        tabview.add("sobre")  
        tabview.set("sobre") 
        #nome do programa
        victory=customtkinter.CTkLabel(master=tabview.tab('sobre'),text='victory-rhythm',text_color='purple',font=customtkinter.CTkFont(size=15))
        victory.place(x=193,y=110)
        #versao do programa
        versao=customtkinter.CTkLabel(master=tabview.tab('sobre'),text='1.0 alpha',text_color='gray')
        versao.place(x=210,y=140)
        #icone
        #aqui vai achar as imagens
        diretorio_icone_main=os.path.dirname(os.path.realpath(__file__))
        pasta=os.path.join(diretorio_icone_main,'imagens')
        imagem_pasta=os.path.join(pasta,'icone_app.png')

        imagem_icone=customtkinter.CTkImage(Image.open(imagem_pasta),size=(100,100))
        icone=customtkinter.CTkLabel(master=tabview.tab('sobre'),text='',image=imagem_icone)
        icone.place(x=190,y=0)
        #aquele textinho sobre o projeto
        texto_sobre=customtkinter.CTkLabel(master=tabview.tab('sobre'),font=customtkinter.CTkFont(size=15),text_color='white',text='''ola, esse e o meu primeiro projeto com o customtkinter e python,
espero que tenha gostado,se esse projeto te interesou
e vc quiser aconpanhar esse projeto ou outros e so
acessar meu github ''')
        texto_sobre.place(x=33,y=170)
        #escrever algo
        diretorio_git_main=os.path.dirname(os.path.realpath(__file__))
        pasta_git=os.path.join(diretorio_git_main,'imagens')
        imagem_git=os.path.join(pasta_git,'git.png')

        git=customtkinter.CTkImage(Image.open(imagem_git),size=(50,40))
        botao_git=customtkinter.CTkButton(master=tabview.tab('sobre'),image=git,text='',fg_color='#242424',width=10,height=10)
        botao_git.place(x=400,y=230)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global atualizador
        self.variavel_banco()#aqui tem as ultimas coisas pra o banco funcionar 
        self.variaveis_funçoes()#aqui e uma forma melhor de organizar as variaveis das funçoed
        mixer.init()#inicia o mixer do pygame
        self.geometry('400x600')
        self.config(background='#242424')
        self.title('victory-rhythm')
        
        self.resizable(width=False,height=False)   #aqui evita que a tela seja redimesionada
        self.player(self.musica_atual)#aqui inicia o player
        self.subtitulo()#aqui configura o nome das musicas e faz aparecer
        self.funçoes_iniciais()#aqui inicia as funçoes necessaria
        self.atualizador()#ele  atualiza tudo desde a imagem da musica ate os contadores
    def variavel_banco(self):
        global session,Base
        self.session=session  
        self.Base=Base
        usu=self.session.query(Caminho).count()#aqui vai retornar o numero 
        self.musica_proxima=list()
        if usu>0:
            n1=self.session.query(Caminho.diretorio).all()
            for c in n1:
                for n in c:
                    self.musica_proxima.append(n)#aqui adiciona as musicas a ser reproduzida
        else:
            self.abrir_pastas()# se nao tiver musica vai abrir a pastas
    def atualizador(self):# aqui esta tendo um bug de a musica atual esta tendo uma duplicata por causa do atualizador 
        global atualizador
        if self.musica_window is None or not self.musica_window.winfo_exists():
            self.after(1000,self.atualizador)
        else:
            
            if atualizador!=self.musica_atual:
                if atualizador=='':
                    atualizador=self.musica_atual
                else:    
                    self.musica_atual=atualizador
                self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300)) 
                self.imagem_fundo.configure(self,text='',image=self.back)
                self.imagem_fundo.place_configure(x=50,y=50)
                #aqui reseta os segundos e os minutos do update label
                self.segundos=self.minutos=0
                self.segundos
                self.update_total()
            #aqui atualiza a duraçao da barra 
                self.duraçao=titulo.info(musica=self.musica_atual)[0]
                self.progresso.set(0)
                #self.barra.configure(variable=self.progresso,to=self.duraçao)
                self.autor=titulo.info(self.musica_atual)[2]
                self.sub_titulo.configure(text=self.autor)
                self.after(1000,self.atualizador) 
            else:
                self.after(1000,self.atualizador) 
    def funçoes_iniciais(self):
        self.botao()#aqui esta os botao proximo e anterior
        self.label()#aqui fica a config da label
        self.backgroud()#aqui pega a capa e coloca no programa
        self.variavel_do_total()#aqui so inicia o label
        self.update_total()#atualizador label do total de segundos da musica
        self.update_barra()#aqui inicia a barra 
        self.update_label()#aqui contabiliza os segundos e atualiza a barra
        self.botao_play()#aqui esta o botao play
        self.botao_janela()#aqui e o botao que abre as opçoes
        self.volume()#aqui esta o volume
    def variaveis_funçoes(self):
        self.segundos=self.minutos=self.hora=0
        self.image_button=customtkinter.CTkButton(master=self,text='')
        self.image_button.place(x=182,y=470)
        self.musica_atual=self.musica_proxima.pop()
        self.progresso=customtkinter.IntVar()
        self.vari=0
        self.n1=1#aqui ativa o botao play
        self.caminhos=list()
        self.end_event=0
        self.end_event2=0
        #self.caminhos.copy()
       
        #print(self.musica_proxima)
        self.musica_anterior=list()
        
        #self.titulo_atual=titulo.info(self.musica_atual)[1]
        #self.title(self.titulo_atual)
        
        self.variavel_volume=customtkinter.DoubleVar(value=0.55)
        self.barra_volume=customtkinter.CTkSlider(self,from_=0,
                                        to=1,
                                    width=100,
                                    border_color='#242424',
                                    bg_color='#242424',variable=self.variavel_volume,
                                    )
        self.barra_volume.place(x=20,y=20)
    def backgroud(self):
        self.fra=customtkinter.CTkFrame(self,bg_color='#242424',width=310,height=310,corner_radius=10)
        self.fra.place(x=45,y=45)
        try:
            self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300)) 
            self.imagem_fundo=customtkinter.CTkLabel(self,text='',fg_color='black',bg_color='#242424',image=self.back)
            self.imagem_fundo.place(x=50,y=50)
        except:
            self.proximo()
    def player(self,musica):#toca a musica
        mixer.init()
        try:
            mixer.music.load(musica)
        except:
            while True:
                try:
                    self.musica_atual=self.musica_proxima.pop()
                    mixer.music.load(self.musica_atual)
                    break
                except:
                    pass
                print()
        mixer.music.play()
    def pausar(self):#pausa a musica
        mixer.music.pause()
    def despausar(self):#despausa a musica
        mixer.music.unpause()    
    def botao(self):#aqui os botoes anterior e proximo
        #botao anterior
        diretorio_main=os.path.dirname(os.path.realpath(__file__))
        pasta=os.path.join(diretorio_main,'imagens')
        imagem_botao=os.path.join(pasta,'anterior.png')
        botao_a = customtkinter.CTkImage(Image.open(imagem_botao),
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
        diretorio_main1=os.path.dirname(os.path.realpath(__file__))
        pasta1=os.path.join(diretorio_main1,'imagens')
        imagem_botao1=os.path.join(pasta1,'proximo.png')
        botao_p = customtkinter.CTkImage(Image.open(imagem_botao1),
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
        n1=self.n1#vai verificar se e pause ou o botao play
        
        self.image_button.destroy()
        if n1%2==0:
            self.pausar()
            diretorio_pause_main=os.path.dirname(os.path.realpath(__file__))
            pasta_pause=os.path.join(diretorio_pause_main,'imagens')
            imagem_botao_pause=os.path.join(pasta_pause,'play1.png')
            self.button_image = customtkinter.CTkImage(Image.open(imagem_botao_pause), size=(30, 30)) 
            self.image_button = customtkinter.CTkButton(master=self,
                                                anchor='center',
                                                image=self.button_image,
                                                width=10,
                                                height=10,
                                                text='',
                                                fg_color='#242424',
                                                command=self.botao_play,
                                                bg_color='#242424',font=("Arial",44))
            
            self.n1+=1
            self.image_button.place(x=177,y=470)
            
        else:
            self.despausar()
            diretorio_play_main=os.path.dirname(os.path.realpath(__file__))
            pasta_play=os.path.join(diretorio_play_main,'imagens')
            imagem_botao_play=os.path.join(pasta_play,'pause.png')
            self.button_image = customtkinter.CTkImage(Image.open(imagem_botao_play), size=(32, 32))
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
            self.image_button.place(x=177,y=470)      
    def label(self):# aqui esta tudo ok
        self.texto=ctk.CTkLabel(self,text='',bg_color='#242424',text_color='black')
        self.texto.place(x=50,y=450)
    def update_label(self,segundos=0,hora=0,minutos=0):
        if mixer.music.get_busy():
            #aqui vai adicionar os segundos e a variavel da barra e tentar deixar sicronizado um com o outro
            self.segundos+=1
            self.vari=self.progresso.get()
            #print(self.segundos)
            self.vari+=1
            self.progresso.set(self.vari)
            
        else:
            self.end_event=self.progresso.get()
            self.end_event2=mixer.music.get_pos()
            if self.end_event>=self.duraçao :# aqui vai verificar o termino da musica com base na barra 
                self.proximo()
            elif self.end_event2==-1:
                self.proximo()
        if self.segundos==60:
            self.segundos=0
            self.minutos+=1
        elif self.segundos>60:
            while self.segundos>60:
                self.segundos-=60
                self.minutos+=1 
        if self.segundos<10 and self.minutos<10:
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
        if self.duraçao=='r':
            try:
                mixer.music.load(self.musica_atual)
            except:
                usu=session.query(Caminho).filter_by(diretorio=self.musica_atual).first()
                self.session.delete(usu)
                self.session.commit()
                try:
                    self.proximo()
                except:
                    try:
                        self.anterior()
                    except:
                        self.anterior    
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
    def abrir_pastas(self):#aqui abre as pastas
        try:
            self.abrir_diretorio=filedialog.askdirectory(title='abra a pasta de suas musicas')
            self.variavel_do_verificador(self.abrir_diretorio)
        except:
            print('erro nas pastasaa')    
    def tirar_musica(self):#tira as musicas
        mixer.music.unload()   
    def reiniciar_musica():#aqui reinicia as musicas
        mixer.music.rewind()    
    def proximo(self):#aqui e onde a magica acontece e faz a musica ir pra outra
        global atualizador
        if len(self.musica_proxima)>=1:
            #print(len(self.musica_atual))
            try:
                if len(self.musica_proxima)!=0:
                    self.musica_anterior.append(self.musica_atual)
                    self.tirar_musica()
                    self.musica_atual=str(self.musica_proxima.pop())
                if '\n' in self.musica_atual:
                    self.musica_atual=self.musica_atual.replace('\n','')
    
                try:
                    
                    mixer.music.load(self.musica_atual)
                    #print(self.musica_atual)
                    pygame.mixer.music.play()
                    
                except:
                    while True:
                        try:
                            self.musica_atual=self.musica_proxima.pop()
                            mixer.music.load(self.musica_atual)
                            break
                        except:
                            pass
                    mixer.music.play()    
                    
                if self.n1%2==0:
                    pass
                else:
                    self.botao_play()
                self.update_total()
               
            #aqui serve pra atualizar a capa das musicas
                atualizador=self.musica_atual
                try:
                    self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300))
                except:
                    return
                self.update_total()    
                self.imagem_fundo.configure(self,text='',image=self.back)
                self.imagem_fundo.place_configure(x=50,y=50)
                
            #aqui reseta os segundos e os minutos do update label
                self.segundos=self.minutos=self.hora=0
            #atualiza o titulo da janela
                
                
            #aqui atualiza a duraçao da barra 
                self.duraçao=titulo.info(musica=self.musica_atual)[0]
                self.progresso.set(0)
                self.barra.configure(variable=self.progresso,to=self.duraçao)
                self.autor=titulo.info(self.musica_atual)[2]
                self.sub_titulo.configure(text=self.autor)
                

            except IndexError:
                print('sem musica')
                print('='*50)
           # print(self.musica_anterior)
                print('='*50)
            #print(self.musica_atual)
        else:
            print('sem musica')    
    def anterior(self): #aqui vai acionar a musica anterior e atualizar tudo
        global atualizador
        try:
            if len(self.musica_anterior)!=0:
                self.musica_proxima.append(self.musica_atual)
                self.tirar_musica()    
                self.musica_atual=str(self.musica_anterior.pop())
            if '\n' in self.musica_atual:
                self.musica_atual=self.musica_atual.replace('\n','')
            try:
                agora=titulo.info(self.musica_atual)
                #print(self.musica_atual,'oie')
                mixer.music.load(self.musica_atual)
                pygame.mixer.music.play()
            except:
                while True:
                    try:
                        self.musica_atual=self.musica_anterior.pop()
                        mixer.music.load(self.musica_atual)
                        break
                    except:
                        pass
                mixer.music.play()
            if self.n1%2==0:
                pass
            else:
                self.botao_play()
            self.update_total()   
            atualizador=self.musica_atual
            #pega a nova capa e coloca
            try:
                self.back=customtkinter.CTkImage(titulo.capa(self.musica_atual),size=(300,300))
            except:
                return  
            self.imagem_fundo.configure(self,text='',image=self.back)
            self.imagem_fundo.place_configure(x=50,y=50)
            #reseta os segundos 
            self.segundos=self.minutos=self.hora=0
            #atualiza o titulo da janela
            
            #aqui atualiza a duraçao da barra
            self.duraçao=titulo.info(musica=self.musica_atual)[0]
            self.progresso.set(0)
            self.barra.configure(to=self.duraçao,variable=self.progresso)


            self.autor=titulo.info(self.musica_atual)[2]
            self.sub_titulo.configure(text=self.autor)
        except IndexError:
            print('sem musica')   
            print('='*50) 
            #print(self.musica_proxima)
            print('='*50)
            #print(self.musica_atual)  
    def open_toplevel(self):#aqui verifica se a janela esta aberta ou nao e a abre se estiver fechada
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()
    def botao_janela(self):  #aqui coloca o botao da opçoes
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
            elif opcoes=='Adicionar musica':
                self.abrir_pastas()
            else:
                self.open_toplevel()   
        optionmenu = customtkinter.CTkOptionMenu(master=self, values=["Opçoes","Musicas",'Adicionar musica',"Geral"],width=50,
                                            command=optionmenu_callback,bg_color='#242424')
        optionmenu.set("opçoes")
        optionmenu.place(x=320,y=10)
    def musicas(self):#aqui vai verificar se a janela musica esta aberta 
        if self.musica_window is None or not self.musica_window.winfo_exists():
            self.musica_window = musica_window(self)
            self.atualizador()  # create window if its None or destroyed
        else:
            self.musica_window.focus()  # if window exists focus it
    def update_barra(self):#tudo ok
        #infomaçoes da barra
        self.vari=self.progresso.get()
        #print(self.progresso.get())
        #self.vari+=1
        self.progresso.set(self.vari)
        #print(self.vari)
        
        self.barra=customtkinter.CTkSlider(self,from_=0,
                                    to=self.duraçao,
                                    width=360,
                                    variable=self.progresso,
                                    border_color='#242424',
                                    bg_color='#242424'
                                    ,command=lambda n1:self.progresso_atual())
        self.barra.place(x=20,y=430)
    def volume_barra(self):#volume
        self.barra=customtkinter.CTkSlider(self,from_=0,
                                    to=1.0,
                                    width=360,
                                    variable=self.progresso,
                                    border_color='#242424',
                                    bg_color='#242424'
                                    ,)
        self.barra.place(x=20,y=430)    
    def progresso_atual(self):#aqui mostra o tempo real
        self.progresso.set(self.progresso.get())
        if mixer.music.get_busy():
            mixer.music.set_pos(self.progresso.get())
            self.segundos=self.minutos=self.horas=0
            
            self.segundos=self.progresso.get()
            self.segundos+=1
            self.vari=self.progresso.get()
            self.vari+=1
            self.progresso.set(self.vari)
            #print(self.vari,self.segundos)
        else:
            pass
        if self.segundos==60:
            self.segundos=0
            self.minutos+=1
        elif self.segundos>60:
            while self.segundos>60:
                self.segundos-=60
                self.minutos+=1 
        if self.segundos<10 and self.minutos<10:
            self.texto.configure(text = f'0{self.hora}:0{self.minutos}:0{self.segundos}\r')
        elif self.segundos<10 and self.minutos>=10:
            self.texto.configure(text = f'0{self.hora}:{self.minutos}:0{self.segundos}')
        elif self.segundos>=10 and self.minutos<10:
            self.texto.configure(text = f'0{self.hora}:0{self.minutos}:{self.segundos}')
        elif self.segundos>=10 and self.minutos>=10:
            self.texto.configure(text = f'0{self.hora}:{self.minutos}:{self.segundos}')
    def subtitulo(self):#aqui onde pega a musica atual e coloca na label
        self.autor=titulo.info(self.musica_atual)[2]
        self.sub_titulo=customtkinter.CTkLabel(self,text=self.autor,font=customtkinter.CTkFont(size=15),fg_color='#242424',text_color='black',width=400)
        self.sub_titulo.place(x=00,y=400)
    def volume(self):#aqui seta o volume
        
        mixer.music.set_volume(self.variavel_volume.get())
        self.after(1000,self.volume)
    def verificador(self):#aqui vai verificar as pastas e os arquivos
        for c in self.lista_dir:
            junçao=self.caminhos+'/'+c
            if os.path.isfile(junçao):
                self.arquivos.append(junçao)
            elif os.path.isdir(junçao):
                self.pastas.append(junçao)
    def separador(self):#aqui vai verificar os arquivos de musica
        for c in self.arquivos:
            if '.mp3' in c :
                self.mp3.add(c)
    def variavel_do_verificador(self,pasta):#aqui so inicia as variaveis do verificador
        self.caminhos=pasta
        self.lista_dir=os.listdir(self.caminhos)
        self.arquivos=list()
        self.pastas=list()
        self.mp3=set()
        self.verificador()
        self.separador()
        while len(self.pastas)>0:
            self.caminhos=self.pastas.pop()
            self.lista_dir=os.listdir(self.caminhos)
            self.verificador()
            self.separador()
        print(self.mp3)    
        self.adicionar_banco()
    def adicionar_banco(self):#aqui adiciona as musicas no banco de dados
        for c in self.mp3:
            n1=c.replace('\n','')
            n3=titulo.info(n1)[2]
            self.caminho=Caminho(name=n3,diretorio=n1)
            self.session.add(self.caminho)
            self.session.commit()   
app=App()    
app.mainloop()