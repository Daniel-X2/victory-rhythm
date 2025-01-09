import asyncio
from shazamio import Shazam
import wget
import os.path
import os
n1=0
def capa(musica):
    try:
        async def main():
            global n1
            shazam = Shazam()
    
            out = await shazam.recognize(musica)  #
            for c in out['track'].items():
                if 'images' in c:
                    n1=c[1]['background']
                    #tela de fundo     
                
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        return 0    
    def download_image(url, save_as):
        wget.download(url, save_as)

    image_url = n1
    save_as = 'imagem.jpg'
    try:
        if os.path.exists(save_as):
            os.remove(save_as)
            download_image(image_url, save_as)

        else:
            download_image(image_url, save_as)
    except:
        return 0
