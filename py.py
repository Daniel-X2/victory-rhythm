from capas import titulo
import customtkinter as ctk 
import customtkinter 
class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self,text='',height=500)
        self.label.grid(row=0, column=0, padx=20)
        self.n4=300
        self.teste()
        self.criar()
    def teste(self):
        n1=open('caminho.txt','r')
        self.n2=list()
        self.dici=dict()
        for c in n1.readlines():
            n1=c.replace('\n','')
            n3=titulo.info(n1)[2]
            self.n2.append(n3)
            self.dici[n1]=n3
        if len(self.n2)>0:
            self.criar()
        print(self.dici)
    def criar(self):
        n1=customtkinter.CTkButton(self,text=self.n2.pop())
        n1.place(x=10,y=self.n4)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")




        self.geometry("400x400")
        self.resizable(width=False,height=False)
        self.config(background='#242424')
        #self.teste()
        
        #self.musica='/home/danields/Desktop/projetos/player_musica/kendrik.mp3'
        #scrol=customtkinter.CTkScrollableFrame(self,width=380,height=380)
        #scrol.place(x=3,y=7)
    def teste(self):
        n1=open('caminho.txt','r')
        self.n2=list()
        self.dici=dict()
        for c in n1.readlines():
            n1=c.replace('\n','')
            n3=titulo.info(n1)[2]
            self.n2.append(n3)
            self.dici[n1]=n3
        print(self.dici)
    
app=App()
app.mainloop()