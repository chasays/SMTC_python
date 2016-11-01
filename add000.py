#!/usr/bin/env python
#coding: utf-8
# Give picture setting a nunber and color.
from _ast import Add

from PIL import Image, ImageDraw, ImageFont
import sys, os
import random

#variable


filePath = sys.path[0]
fileName = "0000.png"
completePath = filePath + '/' + fileName
fontPath = filePath + '/' + "front.ttf"
randomNum = random.randint(0, 100)
print randomNum

localImage = Image.open(completePath)

startDraw = ImageDraw.Draw(localImage)
#Acquite pic's size, and make sure front to size
fontSize = min(localImage.size)/4

startFront = ImageFont.truetype(fontPath, fontSize)
startDraw.text((localImage.size[0]-fontSize, 3), str(randomNum), fill=(255,0,0))
localImage.save(filePath + '/' + "new.png", "jpeg")
print fontSize





