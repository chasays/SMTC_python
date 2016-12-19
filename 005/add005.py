#coding: utf-8
import os

from PIL import Image
import sys

ImRe = sys.path[0]
ImDe = ImRe


def processPicture(resource, dest, picName, imageType):
    imageType = 'jpep' if imageType == '.jpg' else 'png'
    im = Image.open(resource + '/' + picName)
    rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0, im.size[1]/1136.0 if im.size[1] > 1136 else 0)
    if rate:
        im.thumbnail((im.size[0] / rate, im.size[1] / rate))
    im.save(dest + picName, imageType)

def run():
    os.chdir(ImRe)
    for i in os.listdir(os.getcwd()):
        postfix = os.path.splitext(i)[1]
        if postfix == '.png' or postfix == '.jpg':
            print ImRe
            processPicture(ImRe, ImDe, i, postfix)

if __name__ == '__main__':
    run()


