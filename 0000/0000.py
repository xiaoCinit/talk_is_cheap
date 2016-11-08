#coding = utf -8

import PIL
from PIL import Image, ImageDraw, ImageFont

number = str(1)
color = (255,0,0)
font = 'arial.ttf'

def writeNumber(number,color,font):
    image = Image.open("1.jpg")
    x,y = image.size
    print x,y
    print type(x)
    font = ImageFont.truetype(font,60)  #set the font type
    draw = ImageDraw.Draw(image)
    draw.text((x-40,y-920),number,color,font)
    #draw = ImageDraw.Draw(image)
    image.save("new.jpg")

writeNumber(number,color,font)