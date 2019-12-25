import binvox_rw
import mcpi.minecraft as minecraft
with open('castle.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

class House():
    def __init__(self,data):
        self.data=data
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0+x,y0+8,z+z0,57)

    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(9):
            for z in range(11):
                mc.setBlock(x0,y+y0,z+z0,41)
                mc.setBlock(x0+10,y+y0,z+z0,41)
        for y in range(9):
            for x in range(10):
                mc.setBlock(x0+x+1,y+y0,z0,41)
                mc.setBlock(x0+x+1,y+y0,z0+10,41)

    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(5):
            mc.setBlock(x0+4,y+y0,z0,0)
            mc.setBlock(x0+5,y+y0,z0,0)

    def window(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(2):
            mc.setBlock(x0+7,y+y0+4,z0,20)
            mc.setBlock(x0+8,y+y0+4,z0,20)
    def statue(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for i in range(len(model.data)):
            for j in range(len(model.data[i])):
                for k in range(len(model.data[i][j])):
                    if model.data[i][j][k] == True:
                        mc.setBlock(x0+k,y0+j,z0+i,41)
                    else:
                        mc.setBlock(x0+k,y0+j,z0+i,0)

import numpy as n
import cv2
import time
import serial
import serial.tools.list_ports
def rectangle_img (frame,w,h):
    frame = cv2.rectangle(frame,(0,0),(w,h),(0,255,0),2)        #x是640，y是480
    frame = cv2.rectangle(frame,(w,h),(2*w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,2*h),(3*w,3*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(0,h),(w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(0,2*h),(w,3*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(w,0),(2*w,h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,0),(3*w,h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,h),(3*w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(w,2*h),(2*w,3*h),(0,255,0),2)

def choose(x0,y0,w,h):
    if x0 < w and y0 < h:
        return 20
    elif x0 > w and x0 < 2*w and y0 < h:
        return 40
    elif x0 > 2*w and x0 < 3*w and y0 < h:
        return 60
    elif x0 < w and y0 > h and y0 < 2*h:
        return 80
    elif x0 > w and x0 < 2*w and y0 > h and y0 < 2*h:
        return 100
    elif x0 > 2*w and x0 < 3*w and y0 > h and y0 < 2*h:
        return 120
    elif x0 < w and y0 > 2*h and y0 < 3 *h:
        return 140
    elif x0 > w and x0 < 2*w and y0 > 2*h and y0 < 3 *h:
        return 160
    elif x0 > 2*w and x0 < 3*w and y0 > 2*h and y0 < 3 *h:
        return 180
    elif x0 == None or y0 == None:
        return 0

face_cascade = cv2.CascadeClassifier(r'D:\Desktop\kaiyuan\work\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'D:\Desktop\kaiyuan\work\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)         #打开摄像机

ret_1,img = cap.read()
print(img.shape)

w = int(img.shape[1]/3)           #长宽
h = int(img.shape[0]/3)

x0 = 1                #初始化x0,y0
y0 = 1
ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
time.sleep(2)                           #不可或缺的休眠让arduino缓冲

count = {}           #记录前几次的脸部位置
count_angle = 0   #记录一定时间内的平均值
while (True):

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    rectangle_img(frame,w,h)                  #将图片变成九宫格

    faces = face_cascade.detectMultiScale(gray,1.3,5)       #人脸识别

    for list_1 in faces:
        x0 = int(list_1[0])
        y0 = int(list_1[1])
    for (x,y,w0,h0) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w0,y+h0),(125,125,125),2)
        roi_gray = gray[y:y+h0,x:x+w0]
        roi_color = frame[y:y+h0,x:x+w0]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print(type(x))                                #x是一个元组中的int

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)        #划分眼睛


    k = choose(x0,y0,w,h)       #x0,y0判定为几度
    print(k,type(k))

    if k in count:
        count[k] += 1
        print(count)
    else:
        count[k] = 1
        print(count)

    if (k in count) and (count[k] == 6):
        ser.write((str(30)+'\n').encode())
        count.clear()


        mc = minecraft.Minecraft.create()
        pos = mc.player.getTilePos()
        position=list(pos)
        position1=list(range(3))
        position2=list(range(3))
        position3=list(range(3))
        position4=list(range(3))
        for i in range(3):
            position1[i]=list(pos)[i]+25
            position2[i]=list(pos)[i]-25
            position3[i]=list(pos)[i]-50
            position4[i]=list(pos)[i]


        position1[1]=list(pos)[1]
        position2[1]=list(pos)[1]
        position3[1]=list(pos)[1]
        position4[1]=list(pos)[1]+20
        mh=House(position)
        mh.wall()
        mh.roof()
        mh.door()
        mh.window()
        mh1=House(position1)
        mh1.wall()
        mh1.roof()
        mh1.door()
        mh1.window()
        mh2=House(position2)
        mh2.wall()
        mh2.roof()
        mh2.door()
        mh2.window()
        mh3=House(position4)
        mh3.statue()
        pos1=list(pos)
        pos1[0]=list(pos)[0]
        pos1[1]=list(pos)[1]
        pos1[2]=list(pos)[2]+75
        mc.player.setTilePos(list(pos1))

    if (k in count) and (count[k] != 6):
        ser.write((str(k)+'\n').encode())                               #仍然有漏洞，没有人脸也会判别

        mc = minecraft.Minecraft.create()
        pos = mc.player.getTilePos()
        pos1=list(pos)
        if m <=90:
            pos1[0]=list(pos)[0]+k*2
            pos1[1]=list(pos)[1]
            pos1[2]=list(pos)[2]
            mc.player.setTilePos(list(pos1))
        else:
            pos1[0]=list(pos)[0]+(90-k)*2
            pos1[1]=list(pos)[1]
            pos1[2]=list(pos)[2]
            mc.player.setTilePos(list(pos1))


    time.sleep(1)

    cv2.imshow('frame',frame)                       #显示图片

    if cv2.waitKey(1) and 0xFF==ord('q'):
        break

cap.release()
cv2.destroyWindow()
