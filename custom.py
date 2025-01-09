import PIL.Image 
import customtkinter as ctk 
import customtkinter 
import PIL 
from PIL import Image,ImageTk 
from capas import backgroud
from capas import titulo
from classe import player
from pygame import mixer
from time import sleep



janela =ctk.CTk()
janela.geometry('400x600') #aqui da o tamanho da tela
janela.resizable(width=False,height=False)   #aqui evita que a tela seja redimesionada


#capa das musicas
back=backgroud.capa()
if back==0:
    capa_musica= customtkinter.CTkImage(Image.open('capa_padrao.jpeg'), size=(300,300))
else:
    capa_musica= customtkinter.CTkImage(Image.open('imagem.jpg'), size=(300,300))


capa=ctk.CTkLabel(janela,image=capa_musica,text='',width=10,height=10,anchor='center')
capa.place(x=45,y=50)


#botao anterior
botao_a = customtkinter.CTkImage(Image.open("anterior.png"), size=(41, 28))
botao_anterior=ctk.CTkButton(janela,image=botao_a,width=10,height=10,text='',fg_color='#242424',bg_color='#242424',)
botao_anterior.place(x=114,y=470)
#botao proximo
botao_p = customtkinter.CTkImage(Image.open("proximo.png"), size=(41,28))
botao_proximo=ctk.CTkButton(janela,text='',image=botao_p,width=10,height=10,fg_color='#242424',bg_color='#242424')
botao_proximo.place(x=231,y=470)



#barra de progresso
progresso=customtkinter.IntVar()
duraçao=titulo.info()[0]

#barra=customtkinter.CTkSlider(janela,from_=0,to=duraçao,width=360,variable=progresso,border_color='#242424',)


def update_barra():
    global progresso
    global duraçao

    barra=customtkinter.CTkSlider(janela,from_=0,to=duraçao,width=360,variable=progresso,border_color='#242424',)
    #mixer.music.set_pos(progresso.get())
    barra.place(x=20,y=440)
    barra.after(1000,update_barra) # chama este método novamente em 1.000 milissegundos
update_barra()         
#mudar de play pra pause
n1=1
n2=0
def mudar ():
    global n1
    global n2
    global button_image
    global image_button
    if n1%2==0:
        player.despausar()
        button_image = customtkinter.CTkImage(Image.open("play1.png"), size=(30, 30)) 
        image_button = customtkinter.CTkButton(master=janela,anchor='center',
    text="",
    image=button_image,
    width=10,
    height=10,
    corner_radius=50,
    fg_color='#242424',command=mudar)
        n1+=1
        image_button.place(x=182,y=470)
    else:
        player.pausar()
        button_image = customtkinter.CTkImage(Image.open("pause.png"), size=(32, 32)) 
        image_button = customtkinter.CTkButton(master=janela,anchor='center',
    text="",
    image=button_image,
    width=10,
    height=10,
    corner_radius=50,
    fg_color='#242424',command=mudar)
        
        n1+=1
        image_button.place(x=182,y=470)
#primeiro play        
button_image = customtkinter.CTkImage(Image.open("play1.png"), size=(30, 30)) 
image_button = customtkinter.CTkButton(master=janela,anchor='center',
    text="",
    image=button_image,
    width=10,
    height=10,
    corner_radius=50,
    fg_color='#242424',command=mudar)

#contador label

milisegundos=0
segundos=0
hora=0
minutos=0
texto=ctk.CTkLabel(janela,text='')
texto.place(x=50,y=450)
duraçao=titulo.info()[0]
autor=titulo.info()[1]
#duraçao atual da musica
def update_label():
    global segundos,minutos,hora,milisegundos
    milisegundos=mixer.music.get_pos()
    if mixer.music.get_busy():
        segundos+=1
    else:
        pass
    if segundos==60:
        segundos=0
        minutos+=1
    elif segundos>60:
        while segundos>60:
            segundos-=60
            minutos+=1 
    if segundos<10 and minutos<10:
        texto.configure(text = f'0{hora}:0{minutos}:0{segundos}')
    elif segundos<10 and minutos>=10:
        texto.configure(text = f'0{hora}:{minutos}:0{segundos}')
    elif segundos>=10 and minutos<10:
        texto.configure(text = f'0{hora}:0{minutos}:{segundos}')
    elif segundos>=10 and minutos>=10:
        texto.configure(text = f'0{hora}:{minutos}:{segundos}')
         
    texto.after(1000,update_label) # chama este método novamente em 1.000 milissegundos    

update_label()


#duraçao total da musica
segundos_total=duraçao
minutos_total=0
horas_total=0
total=ctk.CTkLabel(janela,text='')
total.place(x=300,y=450)
def update_total():
    global segundos_total,minutos_total,horas_total
    if segundos_total==60:
        segundos_total=0
        minutos_total+=1
    elif segundos_total>60:
        while segundos_total>60:
            segundos_total-=60
            minutos_total+=1 
    if segundos_total<10 and minutos_total<10:
        total.configure(text = f'0{horas_total}:0{minutos_total}:0{segundos_total}')
    elif segundos_total<10 and minutos_total>=10:
        total.configure(text = f'0{horas_total}:{minutos_total}:0{segundos_total}')
    elif segundos_total>=10 and minutos_total<10:
        total.configure(text = f'0{horas_total}:0{minutos_total}:{segundos_total}')
    elif segundos_total>=10 and minutos_total>=10:
        total.configure(text = f'0{horas_total}:{minutos_total}:{segundos_total}')

#titulo da musica
janela.title(titulo.info()[1])
update_total()
popup=0
def janela_playlist():
    global popup
    popup=customtkinter.CTkToplevel()
    popup.geometry('400x400')

botao=ctk.CTkButton(janela,command=janela_playlist)
botao.place(x=0,y=0)
player('kendrik.mp3')
while True:
    print(mixer.music.get_pos())
image_button.place(x=182,y=470)#182 450
janela.mainloop() 