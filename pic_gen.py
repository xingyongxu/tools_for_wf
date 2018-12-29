#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import codecs

def pictureDraw():
    W=1600
    H=900
    font=ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf",200)

    n = 0
    with codecs.open("/Users/xingyongxu/Desktop/symbols", 'r', encoding='utf-8') as words:
        for msg in words:
            image = Image.new('RGB', (W, H), (255, 255, 255))
            draw = ImageDraw.Draw(image)
            name = str(n/20 + 1) + '-' + str(n % 20 + 1)
            w, h = draw.textsize(msg, font=font)
            draw.text(((W - w) / 2, (H - h) / 2), msg,font=font,fill=(random.randint(30,120),random.randint(30,120),random.randint(30,120)))
            image.save('./pics/' + name + '.jpg','jpeg')
            #image.show()
            n = n + 1

if __name__=='__main__':
    pictureDraw()
