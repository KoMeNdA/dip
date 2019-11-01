#!/usr/bin/python

import subprocess
from vncdotool import api

import time 

subprocess.call(["./createvm.sh"])

client = api.connect('localhost::5907', password=None)

client.captureScreen("/dip/test/screen/image1.png")

client.keyPress('up')
time.sleep(2)
captureScreen("/dip/test/screen/image2.png")

client.keyPress('enter')
time.sleep(120)

captureScreen("/dip/test/screen/image3.png")

client.mouseMove(500, 600)
time.sleep(1)
client.mousePress(1)
time.sleep(3)

captureScreen("/dip/test/screen/image4.png")

client.keyPress('r')

time.sleep(2)

client.keyPress('u')

time.sleep(2)

client.keyPress('s')

time.sleep(10)

captureScreen("/dip/test/screen/image5.png")

client.mouseMove(500, 230)
client.mousePress(1)

captureScreen("/dip/test/screen/image6.png")

client.mouseMove(950, 750)
client.mousePress(1)

time.sleep(120)

captureScreen("/dip/test/screen/image7.png")

client.mouseMove(1015, 600)
client.mousePress(1)
time.sleep(3)

captureScreen("/dip/test/screen/image2.png")
	
client.mouseMove(450, 550)
client.mousePress(1)

client.mouseMove(45, 55)
time.sleep(2)
client.mousePress(1)


time.sleep(30)

client.mouseMove(950, 720)
client.mousePress(1)

time.sleep(10)

client.mouseMove(250, 180)
client.mousePress(1)
client.mousePress(1)

time.sleep(10)

client.mouseMove(820, 55)
client.mousePress(1)

time.sleep(10)

client.mouseMove(500, 110)
client.mousePress(1)

client.keyPress('r')

time.sleep(2)

client.keyPress('o')

time.sleep(2)

client.keyPress('o')

time.sleep(2)

client.keyPress('t')

time.sleep(3)

client.mouseMove(500, 190)
client.mousePress(1)

time.sleep(3)

client.keyPress('r')

time.sleep(2)

client.keyPress('o')

time.sleep(2)

client.keyPress('o')

time.sleep(2)

client.keyPress('t')

time.sleep(3)

client.mouseMove(45, 50)

time.sleep(2)

client.mousePress(1)

time.sleep(2)

client.mousePress(1)

time.sleep(3600)

client.mouseMove(900, 600)
client.mousePress(1)

time.sleep(600)

subprocess.call(["virsh", "start", "slinux7"])

time.sleep(60)

client.mouseMove(400, 320)
client.mousePress(1)

time.sleep(60)

client.mouseMove(820, 55)
client.mousePress(1)


time.sleep(5)

client.mouseMove(400, 140)
client.mousePress(1)

client.keyPress('a')

time.sleep(2)

client.keyPress('d')

time.sleep(2)

client.keyPress('m')

time.sleep(2)

client.keyPress('i')

time.sleep(2)

client.keyPress('n')

time.sleep(2)

client.mouseMove(365, 275)
client.mousePress(1)

client.mouseMove(45, 80)
client.mousePress(1)

client.mouseMove(1000, 750)
client.mousePress(1)

#def difImage(img)
	






