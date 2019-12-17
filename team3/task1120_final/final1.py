import mcpi.block as block
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()


#房子类
class house():
    def __init__(self,data):
        self.data=data

    def wall(self,blockid):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                for y in range(11):
                    mc.setBlock(x+x0,y+y0,z+z0,blockid)
        for x in range(9):
            for z in range(9):
                for y in range(9):
                    mc.setBlock(x0+1+x,y0+1+y,z0+1+z,block.AIR.id)
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(3):
             mc.setBlock(x0+5,y0+y+1,z0,block.AIR.id)
    def window(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(2):
            for z in range(2):
               mc.setBlock(x0,y0+y+1,z0+3+z,block.GLASS.id) 
    def fire(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
               mc.setBlock(x0+x,y0+10,z0+z,block.GLOWSTONE_BLOCK.id)

               
    #调用build来搭建一个房子
    def build(self,bid):
        self.wall(bid)
        self.window()
        self.door()
        self.fire()

    #可以通过house.isinhouse()来判断角色是否在该房子内
    def isinhouse(self):
        recentpos=mc.player.getTilePos()
        if recentpos.x in range(self.data[0],self.data[0]+11) and recentpos.z in range(self.data[2],self.data[2]+11) and recentpos.y in range(self.data[1],self.data[1]+11):
            return True
        else:
            return False
    
#暂定一共建三个房子，投石机有两个模式，进入第三个房子时程序结束
def mangonelmode1():
    import numpy as np
    import cv2

    import serial
    import serial.tools.list_ports
    import time

    state=-1

    lenth=1024
    width=678
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    ports = list(serial.tools.list_ports.comports())
    print (ports)

    for p in ports:
        print (p[1])
        if "Uno" in p[1]:
            ser=serial.Serial(port=p[0])
        else :
            print ("No Arduino Device was found connected to the computer")

    time.sleep(2)

    def drawface(x,y,w,h,img):
        global state
        fc=x+w/2
        mid=lenth/2
        limit=50
        if fc<mid-limit:
            a=255
            b=0
    #        print('l\n')
            if state!=1:
                state=1
                ser.write('1'.encode())

        elif fc>mid+limit:
            a=0
            b=255
    #        print('r\n')
    #        ser.write(1)
            if state!=2:
                ser.write('2'.encode())
                state=2
        else:
            a=255
            b=255
            if state!=0:
                ser.write('0'.encode())
                state=0
    #        print('toss\n')
    #        ser.write(2)

        cv2.rectangle(img,(0,0),(x,y),(a,b,0),5)
        cv2.rectangle(img,(x,0),(x+w,y),(a,b,0),5)
        cv2.rectangle(img,(x+w,0),(lenth,y),(a,b,0),5)
        cv2.rectangle(img,(0,y),(x,y+h),(a,b,0),5)
        cv2.rectangle(img,(x+w,y),(lenth,y+h),(a,b,0),5)
        cv2.rectangle(img,(0,y+h),(x,width),(a,b,0),5)
        cv2.rectangle(img,(x,y+h),(x+w,width),(a,b,0),5)
        cv2.rectangle(img,(x+w,y+h),(lenth,width),(a,b,0),5)

    def run():
        action = "empty"
        while action != "o":
    #        print ('q for quit,others for command')
            print('o for start, others for test')
            action = input("> ")
            ser.write(action.encode())
            time.sleep(1)
            ser.write("y".encode())
            time.sleep(1)
            ser.write("g".encode())
            time.sleep(1)

       

    run()

    time.sleep(2)

    while(house1.isinhouse()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray=cv2.resize(frame,(lenth,width),interpolation=cv2.INTER_CUBIC)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            drawface(x,y,w,h,gray)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def mangonelmode2():
    pass


place1=[pos.x-20,pos.y,pos.z]
place2=[pos.x+20,pos.y,pos.z]
place3=[pos.x,pos.y,pos.z]

house1=house(place1)
house2=house(place2)
house3=house(place3)

house1.build(block.STONE.id)
house2.build(42)
house3.build(57)
print("进入不同的房间来使投石机进入不同模式")
while True:
    time.sleep(1)
    if house1.isinhouse():
        print('在停留3秒之后进入模式1')
        timer=0
        while house1.isinhouse():
            timer+=1
            print(timer)
            mc.postToChat(timer)
            time.sleep(1)
            if timer==3:
                break
        print("模式1启动,离开房子将立即结束该模式")
        mc.postToChat("mangonelmode1 on")
        while house1.isinhouse():
            mangonelmode1()
        print('模式1结束')
        mc.postToChat("mangonelmode1 off")
    if house2.isinhouse():
        print('在停留3秒之后进入模式2')
        timer=0
        while house2.isinhouse():
            timer+=1
            print(timer)
            mc.postToChat(timer)
            time.sleep(1)
            if timer==3:
                break
        print("模式2启动,离开房子将立即结束该模式")
        mc.postToChat("mangonelmode2 on")
        mangonelmode2()
        print('模式2结束')
        mc.postToChat("mangonelmode2 off")
    if house3.isinhouse():
        print('在停留3秒之后程序将被关闭')
        timer=0
        while house3.isinhouse():
            timer+=1
            print(timer)
            mc.postToChat(timer)
            time.sleep(1)
            if timer==3:
                break
        if timer==3:
            print('程序关闭')
            mc.postToChat("program off")
            break
