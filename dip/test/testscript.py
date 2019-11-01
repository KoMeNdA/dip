#!/usr/bin/python
# -*- coding: utf-8 -*-
#from vncdotool import api


#client = api.connect('localhost::5907', password=None)

#client.mouseMove(820, 55)

from PIL import Image, ImageDraw, ImageChops


#image_1 = Image.open("/dip/test/test_scrin/scrin1.png")
#image_2 = Image.open("/dip/test/test_scrin/scrin2.png")


 
#diff = ImageChops.difference(image_1, image_2)
 
#diff.show()
#print diff
#print len(''.join(sorted(set(diff.tostring()), key=diff.tostring().index)))



#import ImageChops
import math, operator

#def rmsdiff():
    #"Calculate the root-mean-square difference between two images"

    im1 = Image.open("/dip/test/test_scrin/scrin1.png")
    im2 = Image.open("/dip/test/test_scrin/scrin2.png")

    #h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    diff=ImageChops.difference(im1, im2).getbbox()    
#diff=math.sqrt(reduce(operator.add,map(lambda h, i: h*(i**2), h, range(256))) / (float(im1.size[0]) * im1.size[1]))

 print diff
