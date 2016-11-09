#!/usr/bin/env python
#coding: utf-8
# Give picture setting a nunber and color.
from _ast import Add

from PIL import Image, ImageDraw, ImageFont
import sys
import random

#variable

def drawPic(fileName):
    filePath = sys.path[0]
    fileName = fileName
    completePath = filePath + '/' + fileName
    fontPath = filePath + '/' + "front.ttf"
    randomNum = random.randint(0, 100)

    localImage = Image.open(completePath)

    startDraw = ImageDraw.Draw(localImage)
    #Acquite pic's size, and make sure front to size
    fontSize = min(localImage.size)/4

    startFront = ImageFont.truetype(fontPath, fontSize)

    #parameter "text" as string
    startDraw.text((localImage.size[0]-fontSize, 3), str(randomNum), fill=(200,0,0))

    #save Image to local folder
    print "Done...."
    localImage.save(filePath + '/' + "new.png", "jpeg")

drawPic("0000.png")




