
import PIL.Image
from tinytag import Image, TinyTag
import PIL
import io

def info(musica):
    try:    
        tag: TinyTag = TinyTag.get(musica, image=True)
        #image: Image | None = tag.images.any
        artist: str = tag.artist
        duration: str = tag.duration
        album: str = tag.title
        duracao=int(duration)
        nome=artist
        titulo=album
        return duracao,nome,titulo
    except:
        return 'errrro'
def capa(musica):
    tag: TinyTag = TinyTag.get(musica, image=True)
    image: Image | None = tag.images.any.data
    pi = PIL.Image.open(io.BytesIO(image))
    #pi.save(f'{musica}.png')
    #pi.show()
    return pi



