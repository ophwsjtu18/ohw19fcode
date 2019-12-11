import numpy as np
import cv2
import serial
import serial.tools.list_ports
import time
import random
import math


#Arduino Serials
ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
time.sleep(2)
#face detection	    
cap =cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

lastpos=0
currentpos=0
shoot=0

#distance(x):
    

while(True):
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
            x_d=x+w/2-325
            dis=(-0.88*w+220)
            angle=math.atan(x_d/dis)/3.1415926535897*180
            #print(dis)
            #print(angle)
            ser.write(str(int(dis)).encode())
            ser.write(str(int(angle)).encode())
            time.sleep(0.5)
            cv2.imshow('img',img)
        if((lastpos-currentpos)<5):
            shoot+=1
        if(shoot>10):
            ser.write("s".encode())
            time.sleep(2)
            shoot=0
        lastpos=currentpos
        if cv2.waitKey(1)& 0xFF==ord('q'):
            break
    

cap.release()
cv2.destroyAllWindows()
