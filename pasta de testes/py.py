
import customtkinter as ctk 
import customtkinter 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.config(background='#242424')
        self.progresso=customtkinter.DoubleVar()
        self.vari=0
        self.barra()
        
    def barra(self):
        self.vari=self.progresso.get()
        #print(self.progresso.get())
        self.vari+=1
        self.progresso.set(self.vari)
        print(self.progresso.get())
        duraçao=320
        barra=customtkinter.CTkSlider(self,from_=0,
                                    to=duraçao,
                                    width=360,
                                    variable=self.progresso,
                                    border_color='#242424',bg_color='#242424',command=lambda n1:self.progresso.set(self.progresso.get()))
        barra.place(x=20,y=20)
        barra.after(1000,self.barra)
    def teste(self):
            self.vari=self.progresso.get()
app=App()
app.mainloop()