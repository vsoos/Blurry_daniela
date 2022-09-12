# Import required Image library
from PIL import Image, ImageFilter
import random

pictures = ['forest.png', 'northern_lights.png', 'sauna.png']

picture = random.choice(pictures)
print(picture)

x = 60


def blur(picture):
    blurred_image = picture.Filter(ImageFilter.BoxBlur(x))
    result = blurred_image.show()
    return result


blur(picture)
