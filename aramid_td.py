#!/usr/bin/python
# -*- coding: utf-8 -*-

import math, operator
import subprocess
from vncdotool import api
from PIL import Image, ImageChops
import sys
import time
import linecache


def runTest():
    line = linecache.getline("/dip/test1/test_sl.cfg", 1)
   # print(line)
    #nmax = 15
    #print(nmax)
    log_file=open("log_file",'w')
    i=1
    while i <= int(5):
        line = linecache.getline("/dip/test1/test_sl.cfg", i)
        cr_vm= line.split(' ')
        #print(s)
        if cr_vm[0] == "ИмяВМ:":
            name_vm = cr_vm[1]
	    if name_vm != '':
	    	name_vm=name_vm[0:-1]
            	log_file.write("1: Имя виртуальной машины: %s\n" %name_vm)
	    else:
	        log_file.write("1: Имя виртуальной машины НЕ ОПРЕДЕЛЕНО! \n")
		sys.exit()
        elif cr_vm[0] == "ПортВМ:":
            port_vm = cr_vm[1]
	    if port_vm != '':
	   	port_vm=port_vm[0:-1]
            	log_file.write("2: Порт VNC виртуальной машины: %s\n" %port_vm)
            else:
		log_file.write("2: Порт VNC виртуальной машины НЕ ОПРЕДЕЛЕН!")
		sys.exit()
	elif cr_vm[0] == "ХостВМ:":
            host_vm = cr_vm[1]
	    if host_vm != '':
	    	host_vm=host_vm[0:-1]
            	log_file.write("3: Хост виртуальной машины: %s\n" %host_vm)
	    else:
		log_file.write("3: Хост виртуальной машины НЕ ОПРЕДЕЛЕН!")
		sys.exit()
	elif cr_vm[0] == "ПутьДистрибутиваВМ:":
            way_vm = cr_vm[1]
	    if way_vm != '':
	    	way_vm=way_vm[0:-1]
            	log_file.write("4: Путь к дистрибутиву: %s\n" %way_vm)
	    else:
		log_file.write("4: Путь к дистрибутиву НЕ ОПРЕДЕЛЕН!")
		sys.exit()
	elif cr_vm[0] == "ПутьСнимокИсходный:":
            way_screen_src = cr_vm[1]
	    if way_screen_src != '':	
            	way_screen_src = way_screen_src[0:-1]
            	log_file.write("5: Путь к исходным снимкам виртуальной машины: %s\n" %way_screen_src)
	    else:
		log_file.write("5: Путь к исходным снимкам виртуальной машины НЕ ОПРЕДЕЛЕН!")
		sys.exit()
	elif cr_vm[0] == "ПутьСнимокРезультат:":
	    way_screen_rez = cr_vm[1]
	    if way_screen_rez != '':
            	way_screen_rez = way_screen_rez[0:-1]
            	log_file.write("6: Путь к снимкам виртуальной машины, сделанным в процессе тестирования: %s\n" %way_screen_rez)
 	    else:
		log_file.write("6: Путь к снимкам виртуальной машины, сделанным в процессе тестирования НЕ ОПРЕДЕЛЕН!")
        	sys.exit()
	i+=1
    
    fname_cr_vm="./create_vm.sh"
    
    create_vm = ' '.join((fname_cr_vm, name_vm, way_vm, port_vm))

    print(create_vm) 
    if name_vm != '' and port_vm != '' and way_vm != '':
            #start script
	print("Создание виртуальной машины:")
	subprocess.call("%s" % create_vm, shell=True,stdout=subprocess.PIPE)
	#subprocess.call(["%s" % create_vm])
	#ubprocess.Popen([
	log_file.write("7:Создание виртуальной машины!")
        
    else:
        print("Ошибка создания виртуальной машины! ИмяВМ: и(или) ПортВМ и(или) ПутьВМ: НЕ ОПРЕДЕЛЕНЫ!")
        log_file.write("7:Не удалось создать виртуальную машину.") 
    	sys.exit()
	
    if host_vm != '' and port_vm != '':
             #start script
 	add_client='::'.join((host_vm, port_vm))
	print(add_client)
	client=api.connect(add_client, password=None)
        if client == '':
		print("ОШИБКА! Клиент НЕ ОПРЕДЕЛЕН!  ")
                log_file.write("8:Клиент не определен. Проверьте правильно ли организованно соединение.") 
		sys.exit()
	else:
	print("Доступ получен!")
	log_file.write("8:Клиент определен. Доступ получен!.") 
    else:
        print("Ошибка создания виртуальной машины! ИмяВМ: и(или) ПортВМ: НЕ ОПРЕДЕЛЕНЫ!")
	log_file.write("8:Клиент не определен. Проверьте ХостВМ и(или) ПортВМ.")
       	sys.exit()
      
        
    i=1
    n=1
    s=5	
    while i <= int(108):
        line = linecache.getline("/dip/test1/test_sl.cfg", i)
        drive_in = line.split(' ')
        #print(p)
        
        if drive_in[0] == "ПереместитьМышь:":
	  	x=drive_in[1]
		#x=x[0:-1]
		y=drive_in[2]
		y=y[0:-1]
		print(x)
		print(y)
		client.mouseMove(int(x),int(y))
        elif drive_in[0] == "НажатьМышь:":
            	mp=drive_in[1]
		mp=mp[0:-1]
		print(mp)
		client.mousePress(int(mp))
        elif drive_in[0] == "НажатьКлавиатура:":
            	key_pr=drive_in[1]
		key_pr=key_pr[0:-1]
            	print(key_pr)
		client.keyPress(str(key_pr))
        elif drive_in[0] == "Приостановить:":
            	sec=drive_in[1]
		sec=sec[0:-1]
           	print(sec)
		time.sleep(int(sec))
	elif drive_in[0]== "ИсходныйСнимок:":
                src_way=drive_in[1]
               # src_way=src_way[0:-1]
                print(src_way)
		#client.captureScreen(str(src_way))	
		n += 1
        	if drive_in[2]== "СнимокРезультат:":
                	result_way=drive_in[3]
                  	result_way=result_way[0:-1]
                  	print(result_way)
                  	client.captureScreen(result_way)
     		rms=diffImg(result_way, src_way)
		print(rms)
		if int(rms) > 10:
			print("Шаг №%d! ОШИБКА! Тестирование завершено! " % n)
			sys.exit()  
		else:
			print("Шаг №%d! Идем дальше! " % n)
        
 		
	#if drive_in[2]== "ScreenSrc:": 
	#	src_way=drive_in[3]
	#	src_way=src[0:-1]
	#	print(src_way)
	#	client.captureScreen(src_way)
			
	#elif drive_in[3]== "ScreenSrc:":
	#	src_way=drive_in[4]     
        #       src_way=src[0:-1]
        #        print(src_way)
        #        client.captureScreen(src_way)			
 			
        i+=1
    log_file.close()
def diffImg(file1,file2):
    image1 = Image.open(file1)
    print image1
    image2 = Image.open(file2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    h = ImageChops.difference(image1, image2).histogram()
    return math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
runTest()

#def driveTest()
    
    #return 
#def imgDif(img1, img2):
    #return
#def 
