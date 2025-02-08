
import customtkinter
from pygame import mixer
import pygame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        mixer.init()
        
        mixer.music.load('kendrik.mp3')
        mixer.music.play()
        self.geometry("400x400")
        self.config(background='#242424')
        self.variavel_volume=customtkinter.DoubleVar(value=0.55)
        self.barra_volume=customtkinter.CTkSlider(self,from_=0,
                                        to=1,
                                    width=100,
                                    border_color='#242424',
                                    bg_color='#242424',variable=self.vari,
                                    )
        self.barra_volume.place(x=20,y=20)
        
    def volume(self):
        print(self.vari.get())
        mixer.music.set_volume(self.vari.get())
        self.after(1000,self.oi)

app=App()
app.mainloop()        