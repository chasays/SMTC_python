import os

from PIL import Image

Image

def processPicture(resource, dest, picName, imageType):
    imageType = 'jpep' if imageType == 'jpg' else 'png'
    im = Image.open(resource + picName)
    rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0, im.size[1]/1136.0 if im.size[1] > 1136 else 0)
    if rate:
        im.thumbnail((im.size[0] / rate, im.size[1] / rate))
    im.save(dest + picName, imageType)
