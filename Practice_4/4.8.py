from PIL import Image, ImageDraw

name = Image.new("RGB", (800, 350), (9, 23, 33))
draw = ImageDraw.Draw(name)

draw.rectangle((10, 45, 15,288), fill='#18b57b', outline='#5ef7bf', width=1)
draw.arc((-15, 38, 111, 129), -120, 120, fill='#18b57b', width=10)
draw.arc((-40, 128, 170, 295), -120, 120, fill='#18b57b', width=10)

draw.ellipse((170, 200, 270, 295), fill='#18b57b', outline='#5ef7bf', width=1)
draw.ellipse((183, 210, 257, 283), fill='#091721', outline='#5ef7bf', width=1)

draw.rectangle((280, 200, 285, 288), fill='#18b57b', outline='#5ef7bf', width=1)
draw.arc((273, 170, 350, 320), -150, 40, fill='#18b57b', width=7)


draw.rectangle((380, 45, 385,288), fill='#18b57b', outline='#5ef7bf', width=1)
draw.arc((355, 38, 480, 129), -120, 120, fill='#18b57b', width=10)
draw.arc((330, 128, 540, 295), -120, 120, fill='#18b57b', width=10)

draw.rectangle((550, 200, 555, 288), fill='#18b57b', outline='#5ef7bf', width=1)
draw.ellipse((545, 160, 560, 190), fill='#18b57b', outline='#5ef7bf', width=1)

name.save("name.jpg")