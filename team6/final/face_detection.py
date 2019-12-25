import numpy as np
import cv2
import serial
import serial.tools.list_ports
import time
import random
import math
#import mcpi.minecraft as minecraft
#import mcpi.block as block
#from house import House



#Arduino Serials
ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
#time.sleep(2)
#face detection	    
cap =cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

lastpos=0
currentpos=0
lastdis=0
currentdis=0
lastx_d=0
currentx_d=0
shoot=0
#MC
#mc=minecraft.Minecraft.create()
#pos=mc.player.getTilePos()
#pos0=[]
#pos0.append(pos.x)
#pos0.append(pos.y)
#pos0.append(pos.z)
#des=House([pos.x+20,pos.y,pos.z],mc,block.GOLD_BLOCK.id,block.GLASS.id)
#des.buildall()

ct=0
while(True):
    ct+=1
    #到达目的地了吗
    #if(des.isInsideHouse()):
        #mc.postToChat("You win")
        #break
    #人脸识别，一方面投石机追踪，一方面控制MC里面人到Destinatioin
    ret,img=cap.read()
    center=[img.shape[0]/2,img.shape[1]/2]
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    tmp=0
    for(x,y,w,h) in faces:
        tmp+=1
    if(tmp>1):
        print("too many faces")
    else:
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h, x:x+w]
            
            x_d=x+w/2-325-73
            dis=(-0.88*w+220)
            angle=x_d#math.atan(x_d/dis)/3.1415926535897*180
            currentpos=angle
            currentdis=dis
            currentx_d=x_d
            if(ct==1):
                lastpos=currentpos
                lastdis=currentdis
                lastx_d=currentx_d
            #pos=mc.player.getTilePos()
            #mc.player.setTilePos([pos.x+(currentx_d-lastx_d)/5,pos.y,pos.z+(currentdis-lastdis)/5])
            #print(x_d)
            #print(angle)
            #ser.write
            print(str(int(angle)).encode())
            #ser.write
            if(angle<0):
                ser.write(str(int(angle)).encode())
            else:
                ser.write(("+"+str(int(angle))).encode())
            time.sleep(1)
            if((lastpos-currentpos)<10 and abs(angle)<15):
                shoot+=1
        if(shoot>1):
            time.sleep(2)
            #mc.player.setTilePos([0,-1000,0])
            ser.write(str(10000).encode())
            time.sleep(2)
            shoot=0
        lastpos=currentpos
        lastdis=currentdis
        lastx_d=currentx_d
    cv2.imshow('img',img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
