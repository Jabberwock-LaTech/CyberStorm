from PIL import Image

pixellist =[]

im = Image.open("image.png")
imrgb = im.convert("RGB")
for i in range(500):
    for j in range (500):
        pixellist[(i*500)+j] = imrgb.getpixel(i,j)

print pixellist