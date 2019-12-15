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
def mangonelmodel1():
    pass
def mangonelmodel2():
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
        mc.postToChat("mangonelmodel1 on")
        while house1.isinhouse():
            mangonelmodel1()
        print('模式1结束')
        mc.postToChat("mangonelmodel1 off")
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
        mc.postToChat("mangonelmodel2 on")
        while house2.isinhouse():
            mangonelmodel2()
        print('模式2结束')
        mc.postToChat("mangonelmodel2 off")
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
            break
