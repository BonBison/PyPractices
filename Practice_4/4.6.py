from PIL import ImageDraw
from PIL import Image

def board(num, size):
    image = Image.new('1', (num * size, num * size), 1)
    drawer = ImageDraw.Draw(image)
    for x in range(num):
        for y in range(num):
            if (x+y) % 2 == 0:
                drawer.rectangle(((x * size, y * size ), ((x+1) * size - 1, (y +1)* size - 1)), 0)
    image.save('image-4.6.png', 'PNG')

board(100,10)