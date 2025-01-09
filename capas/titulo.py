from tinytag import Image, TinyTag
import time
import threading
def info(musica):
    tag: TinyTag = TinyTag.get(musica, image=True)
    image: Image | None = tag.images.any
    artist: str = tag.artist
    duration: str = tag.duration
    album: str = tag.title
    duracao=int(duration)
    nome=artist
    titulo=album
    return duracao,nome,titulo



