#coding = utf -8

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""
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