from PIL import Image

def make_preview(size, colors):
    img = Image.open("image2.jpg")
    img = img.resize(size)
    img = img.quantize(colors)
    img.save('image-4.9.bmp')

make_preview((888, 444), 69)