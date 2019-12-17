import numpy as np
import cv2
import serial
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(1)

Material=[block.WOOD_PLANKS.id,block.WOOD.id,block.SNOW_BLOCK.id]

pat=[
[1,1,1,1,1,1,1,1,1,1],
[1,3,3,3,3,3,3,3,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,3,1,3,1,3,1],                                   #屋顶的花纹
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,3,3,3,3,3,3,3,1],
[1,1,1,1,1,1,1,1,1,1]]

def house(x0,y0,z0,M=block.SNOW_BLOCK.id,L=10,W=10,H=10,):
    for a in range(0,L):
        for c in range(0,W):
            for b in range(0,H):
                mc.setBlock(x0+a,y0+b,z0+c,M)                 #先填满
    for a in range(0,L-2):
        for c in range(0,W-2):
            for b in range(0,H-1):
                mc.setBlock(x0+1+a,y0+1+b,z0+1+c,0)           #再清除内部
    for a in range(0,L):
        for b in range(0,W):
            if pat[a][b]==1:
                mc.setBlock(x0+a,y0+H,z0+b,block.FIRE.id)        #天花板透明
            else:
                mc.setBlock(x0+a,y0+H,z0+b,block.FIRE.id)
    for a in range(1,3):
        x1=int((2*x0+L)/2)
        mc.setBlock(x1,y0+a,z0,0)                             #造个门
    x1=int(x0+L/4)
    y1=int(y0+H/2)
    mc.setBlock(x1,y1,z0,block.FIRE.id)                                   #开个窗户
 #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx="COM19"
porty="COM9"
#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=9600
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=5
# 打开串口，并得到串口对象
ser=serial.Serial(portx,bps,timeout=timex)
ser1=serial.Serial(porty,bps,timeout=timex)

 # 写数据
result=ser.write("114".encode("gbk"))
print("test:",result)

x0=0
y0=0
tick0=time.time()
tick1=time.time()
the_angle=0
angle=str(the_angle)
x1=0
y1=0
flag=0
while(True):
    ret,frame=cap.read()
    
    #frame = cv2.imread('frame')
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    #print(faces)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        the_angle=-90+180*(x/640)
        angle=str(the_angle)
        x1=x
        y1=y

    cv2.imshow('frame',frame)
    if(abs(x1-x0)<50) and (abs(y1-y0)<50):
       tick1=time.time()
       if tick1-tick0>=3 and flag==0:
            pos=mc.player.getTilePos()
            result1=ser1.write("114".encode("gbk"))
            
            result=ser.write("114".encode("gbk"))
            
            print("已发射！")
            mc.postToChat("Fire!")
            house(pos.x,pos.y,pos.z,Material[0])
            flag=1
    else:
        x0=x1
        y0=y1
        tick0=time.time()
        flag=0
        result=ser.write(angle.encode("gbk"))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
