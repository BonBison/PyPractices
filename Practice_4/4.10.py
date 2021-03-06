from PIL import Image

def grey(filename):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y))

    for i in range(x):
        for j in range(y):
            r, g, b = im.getpixel((i, j))
            res.putpixel((i, j), ((r + g + b) // 3, (r + g + b) // 3, (r + g + b) // 3))
    res.save("image-4.10-grey.jpg")


def inversion(filename):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y))
    for i in range(x):
        for j in range(y):
            r, g, b = im.getpixel((i, j))
            res.putpixel((i, j), (255 - r, 255 - g, 255 - b))
    res.save("image-4.10-inversion.jpg")


def contrast(filename):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y))
    for i in range(x):
        for j in range(y):
            r, g, b = im.getpixel((i, j))
            res.putpixel((i, j), (r * 2, g * 2, b * 2))
    res.save("image-4.10-contrast.jpg")


print("Какой фильтр вы хотите наложить на фото?")
print("1. Оттенок серого;")
print("2. Инверсия;")
print("3. Контраст.")

n = int(input("Введите номер: "))

if n == 1:
    grey("image3.jpg")
if n == 2:
    inversion("image3.jpg")
if n == 3:
    contrast("image3.jpg")