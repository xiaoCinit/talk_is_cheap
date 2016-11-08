# -*- coding: UTF-8 -*-

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""
import PIL #第一个坑， PIL库安装一直失败，改为 安装pillow之后成功
from PIL import Image, ImageDraw, ImageFont

number = str(1)
color = (255,0,0)
font = 'arial.ttf'   #自己选择的字体，没有也可以

def writeNumber(number,color,font):
    image = Image.open("1.jpg")
    x,y = image.size
    #print x,y
    #print type(x)
    font = ImageFont.truetype(font,60)  #set the font type
    draw = ImageDraw.Draw(image)
    draw.text((x-40,y-920),number,color,font)  #加入字体，包含的参数顺序(位置，内容，颜色，字体)
    #draw = ImageDraw.Draw(image)
    image.save("new.jpg")   #保存图片

writeNumber(number,color,font)
