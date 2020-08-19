'''x='b'*4
y='a'*5

if x==y:
    print("Equal")

elif x<y:
    print("Less")

elif x>y:
    print("Greater")
***********************************'''

from PIL import Image

image = Image.open(r"image.png")

image.thumbnail((128,128))

image.save('thumb.png')
