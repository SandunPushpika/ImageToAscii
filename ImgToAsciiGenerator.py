import math
from PIL import Image, ImageDraw

file = open("imgtoascii.txt","w")
im = Image.open('Images/car2.jpg')
width, height = im.size

charWidth = 8
charHeight = 18

im = im.resize((int(width*0.3), int(height*0.3*(charWidth/charHeight))),Image.NEAREST)
width, height = im.size
photo = im.load()

charlist = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."[::-1]
smallCharlist = "#Wo- "
arr = list(charlist)
arrLen = len(arr)

def getLetterForColor(color):
    position = math.floor((arrLen/256) * color)
    return arr[position]

newimg = Image.new("RGB",(width*charWidth,height*charHeight),(0,0,0))

draw = ImageDraw.Draw(newimg)

for y in range(height):
    for x in range (width):
        r,g,b = photo[x,y]
        mean = int(r/3 + b/3 + g/3)
        character = getLetterForColor(mean)
        file.write(character)
        draw.text((x*charWidth, y*charHeight), character,(r,g,b))
    file.write('\n')

newimg.save("girl.jpg")
file.close()
