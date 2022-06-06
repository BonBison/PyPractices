from PIL import Image

def makeanagliph(filename, delta):
    image = Image.open(filename)
    x, y = image.size

    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = image.load()

    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
                pixels2[i, j] = r, g, b
    res.save("image-4.7.jpg")

makeanagliph('image.jpg', 50)