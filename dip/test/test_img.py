#!/usr/bin/python
# -*- coding: utf-8 -*-

import math, operator
from PIL import Image, ImageChops
#def main():



def compare(file1,file2):
    image1 = Image.open(file1)
   # print image1
    image2 = Image.open(file2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    #h = ImageChops.difference(image1, image2).histogram()
    return math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    #return math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(image1.size[0]) * image1.size[1]))

def main():    
	cs=compare("/dip/test/test_scrin/scrin1.png", "/dip/test/test_scrin/scrin2.png")
    	print(cs)
	
	if cs != 0:
		print ("ERROR")
	else:
		print("GO")

main()
    


   # if cs>=0:
	#print('ERROR')
	#subprocess.call(["virsh", " shutdown", "slinux7"])
    #else: 
	#print('Step 1: OK!')
	





