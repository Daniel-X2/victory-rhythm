from tinytag import TinyTag
from PIL import Image
import io

tag = TinyTag.get("kendrik.mp3", image=True)
img = tag.images.any.data
print(img)
pi = Image.open(io.BytesIO(img))
# Save as PNG, or JPEG
pi.save('cover.png')
# Display
pi.show()

