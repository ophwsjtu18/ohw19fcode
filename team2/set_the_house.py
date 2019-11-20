from mcpi.minecraft import Minecraft
import time
import block as block
mc = Minecraft.create()
pos = mc.player.getTilePos()

class SMITHY():
    def __init__(self,data):
        self.data = data
    
    def ground(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0,z0+z,98)
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0+5,z0+z,1)
    
    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for y in range(5):
                    mc.setBlock(x0+x,y0+y,z0,1)
                    mc.setBlock(x0+x,y0+y,z0+10,1)
                    mc.setBlock(x0,y0+y,z0+x,1)
                    mc.setBlock(x0+10,y0+y,z0+x,1)
    
    def decoration_smithy(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]

        for x in range (6):
            for y in range(3):
                mc.setBlock(x0+3+x,y0+2+y,z0,20)

        mc.setBlock(x0+1,y0+1,z0,block.AIR.id)
        mc.setBlock(x0+1,y0+2,z0,block.AIR.id)#doorwithtorch
        

        mc.setBlock(x0+5,y0+5,z0+5,89)#stone to light

        for x in range(11):
            mc.setBlock(x0+x,y0+5,z0,43)
            mc.setBlock(x0+x,y0+5,z0+10,43)
            mc.setBlock(x0,y0+5,z0+x,43)
            mc.setBlock(x0+10,y0+5,z0+x,43)#stone slab

        for x in range(11):
            mc.setBlock(x0+x,y0+6,z0,50)
            mc.setBlock(x0+x,y0+6,z0+10,50)
            mc.setBlock(x0,y0+6,z0+x,50)
            mc.setBlock(x0+10,y0+6,z0+x,50)#torch
        
        for x in range(9):
            for z in range(2):
                mc.setBlock(x0+1+x,y0+1,z+z0+8,98)#set

        for x in range(9):
            for y in range(3):
                mc.setBlock(x0+1+x,y0+2+y,z0+8,101)#set fence
        for x in range(9):
            for y in range(3):
                mc.setBlock(x0+1+x,y0+2+y,z0+9,block.LAVA.id)#set lava

        for x in range(8):
            mc.setBlock(x0+2+x,y0+1,z0+7,62)#set furnace
        
        mc.setBlock(x0+1,y0+2,z0+7,54)#set CHEST
        mc.setBlock(x0+1,y0+1,z0+7,84)#set music

        for x in range(3):
            mc.setBlock(x0+5,y0+1,z0+1+x,98)#POOL BOUND 1 

        for x in range(4):
            mc.setBlock(x0+6+x,y0+1,z0+3,98)#pool bound 2 

        for x in range(4):
            for z in range(2):
                mc.setBlock(x0+6+x,y0+1,z0+1+z,block.WATER_STATIONARY.id)#pool water
                mc.setBlock(x0+6+x,y0+2,z0+1+z,111)#pool lily

        for x in range(4):
            mc.setBlock(x0+9-x,y0+2,z0+3,145)#tiezhen

        for x in range(2):
            for z in range(1):
                mc.setBlock(x0+8+x,y0+1,z0+4,87)
                mc.setBlock(x0+8+x,y0+2,z0+4,51)#fire

        for x in range (2):
            mc.setBlock(x0+7,y0+1,z0+4+x,139)
            mc.setBlock(x0+8+x,y0+1,z0+5,139)#fire bound
            
    def smithy(self):
        self.roof()
        self.wall()
        self.ground()
        self.decoration_smithy()

    def clean(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for y in range(5):
                for z in range(11):
                    mc.setBlock(x+x0-2,y+y0+1,z+z0-2,block.AIR.id)



class PUMPKIN():
    def __init__(self,data):
        self.data = data
    
    def ground(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0,z0+z,41)
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0+11,z0+z,41)
    
    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for y in range(11):
                    mc.setBlock(x0+x,y0+y,z0,41)
                    mc.setBlock(x0+x,y0+y,z0+10,41)
                    mc.setBlock(x0,y0+y,z0+x,41)
                    mc.setBlock(x0+10,y0+y,z0+x,41)
    
    def decoration_pumukin(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]

        mc.setBlock(x0+1,y0+1,z0,block.AIR.id)
        mc.setBlock(x0+1,y0+2,z0,block.AIR.id)#doorwithtorch            
    
        for x in range(7):
            mc.setBlock(x0+2+x,y0+4,z0,11)
            mc.setBlock(x0+2+x,y0+4,z0-1,20)
            mc.setBlock(x0+2+x,y0+4,z0+1,20)#horizental
        for x in range(2):
            mc.setBlock(x0+2,y0+5+x,z0,11)
            mc.setBlock(x0+5,y0+5+x,z0,11)
            mc.setBlock(x0+8,y0+5+x,z0,11)
            mc.setBlock(x0+2,y0+5+x,z0-1,20)
            mc.setBlock(x0+5,y0+5+x,z0-1,20)
            mc.setBlock(x0+8,y0+5+x,z0-1,20)
            mc.setBlock(x0+2,y0+5+x,z0+1,20)
            mc.setBlock(x0+5,y0+5+x,z0+1,20)
            mc.setBlock(x0+8,y0+5+x,z0+1,20)#vertical

        for x in range(2):
            for y in range(2):
                mc.setBlock(x0+2+y,y0+8+x,z0,11)
                mc.setBlock(x0+7+y,y0+8+x,z0,11)
                mc.setBlock(x0+2+y,y0+8+x,z0-1,20)
                mc.setBlock(x0+7+y,y0+8+x,z0-1,20)
                mc.setBlock(x0+2+y,y0+8+x,z0+1,20)
                mc.setBlock(x0+7+y,y0+8+x,z0+1,20)#eyes
        
        mc.setBlock(x0+5,y0+11,z0+5,91)#top
        mc.setBlock(x0+5,y0+6,z0-1,91)#nose

        mc.setBlock(x0+9,y0+10,z0+9,91)
        mc.setBlock(x0+1,y0+10,z0+9,91)
        mc.setBlock(x0+9,y0+10,z0+1,91)
        mc.setBlock(x0+1,y0+10,z0+1,91)

        mc.setBlock(x0+9,y0+1,z0+9,91)
        mc.setBlock(x0+1,y0+1,z0+9,91)
        mc.setBlock(x0+9,y0+1,z0+1,91)#room lighting pumpkin

        mc.setBlock(x0+8,y0+1,z0+9,30)
        mc.setBlock(x0+8,y0+1,z0+9,30)
        mc.setBlock(x0+9,y0+2,z0+9,30)
        mc.setBlock(x0+9,y0+1,z0+2,30)
        mc.setBlock(x0+8,y0+10,z0+9,30)
        mc.setBlock(x0+9,y0+9,z0+9,30)
        mc.setBlock(x0+9,y0+10,z0+8,30)
        mc.setBlock(x0+1,y0+7,z0+9,30)
        mc.setBlock(x0+2,y0+7,z0+9,30)#cobweb



        for x in range(3):
            mc.setBlock(x0+4+x,y0,z0+9,87)
            mc.setBlock(x0+4+x,y0+1,z0+9,block.FIRE.id)
            mc.setBlock(x0+4+x,y0+1,z0+7,49)

        mc.setBlock(x0+3,y0+1,z0+9,113)
        mc.setBlock(x0+7,y0+1,z0+9,113)
        for x in range(5):
            mc.setBlock(x0+3+x,y0+1,z0+8,113)
            mc.setBlock(x0+3+x,y0+3,z0+9,87)

        mc.setBlock(x0+3,y0+4,z0+9,87)
        mc.setBlock(x0+5,y0+4,z0+9,87)
        mc.setBlock(x0+7,y0+4,z0+9,87)

        mc.setBlock(x0+3,y0+5,z0+9,51)
        mc.setBlock(x0+5,y0+5,z0+9,51)
        mc.setBlock(x0+7,y0+5,z0+9,51)
        mc.setBlock(x0+4,y0+4,z0+9,51)
        mc.setBlock(x0+6,y0+4,z0+9,51)#inside fire


        for x in range(2):
            for y in range(2):
                mc.setBlock(x0+3+x,y0+6+y,z0+9,87)
                mc.setBlock(x0+6+x,y0+6+y,z0+9,87)

        for x in range(2):
            mc.setBlock(x0+3+x,y0+8,z0+9,51)
            mc.setBlock(x0+6+x,y0+8,z0+9,51)

        mc.setBlock(x0+5,y0+1,z0+6,49)
        mc.setBlock(x0+5,y0+2,z0+7,116)
        mc.setBlock(x0+6,y0+2,z0+7,50)
        mc.setBlock(x0+4,y0+2,z0+7,50)
        mc.setBlock(x0+5,y0+2,z0+6,50)


    
    def pumpkin(self):
        self.roof()
        self.wall()
        self.ground()
        self.decoration_pumukin() 


    
    def clean(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(15):
            for y in range(15):
                for z in range(15):
                    mc.setBlock(x+x0-2,y+y0+1,z+z0-2,block.AIR.id)

    
class HOME():
    def __init__(self,data):
        self.data = data
    
    def ground(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(7):
            for z in range(8):
                    mc.setBlock(x0+x,y0,z0+z,98)
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(7):
            for z in range(8):
                    mc.setBlock(x0+x,y0+5,z0+z,98)
    
    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(7):
            for y in range(6):
                mc.setBlock(x0+x,y0+y,z0,98)
                mc.setBlock(x0+x,y0+y,z0+7,98)
        for y in range(6):
            for z in range(8):
                mc.setBlock(x0,y0+y,z0+z,98)
                mc.setBlock(x0+6,y0+y,z0+z,98)

    def clean(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(12):
            for y in range(15):
                for z in range(12):
                    mc.setBlock(x+x0-1,y+y0+1,z+z0-1,block.AIR.id)

    
    def decoration_home(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]

        mc.setBlock(x0+1,y0+1,z0,block.AIR.id)
        mc.setBlock(x0+1,y0+4,z0,89)
        mc.setBlock(x0+1,y0+2,z0,block.AIR.id)#doorwithtorch

        for y in range(3):
            for x in range(5-2*y):
                for z in range(8):
                    mc.setBlock(x0+x+1+y,y0+6+y,z0+z,98)
        for x in range(5):
            for z in range(10):
                mc.setBlock(x0+x-1,y0+5+x,z0+z-1,5)
                mc.setBlock(x0-x+7,y0+5+x,z0+z-1,5)#roof

        for x in range(3):
            mc.setBlock(x0+x+2,y0+6,z0,57)
            mc.setBlock(x0+x+2,y0+6,z0+7,57)

        mc.setBlock(x0+3,y0+7,z0,57)
        mc.setBlock(x0+3,y0+7,z0+7,57)

        for x in range(3):
            for y in range(2):
                mc.setBlock(x0+x+3,y0+3+y,z0,block.GLASS.id)
        for x in range(2):
            for y in range(2):
                mc.setBlock(x0,y0+2+y,z0+3+x,block.GLASS.id)#WINDOW
        
        mc.setBlock(x0+5,y0,z0+6,87)
        mc.setBlock(x0+5,y0+1,z0+6,block.FIRE.id)
        mc.setBlock(x0+5,y0+2,z0+6,44)
        mc.setBlock(x0+4,y0+1,z0+6,113)
        mc.setBlock(x0+5,y0+1,z0+5,113)
        mc.setBlock(x0+4,y0+1,z0+5,113)


        for x in range(5):
            for y in range(5):
                mc.setBlock(x0+1+x,y0+5,z0+1+y,block.AIR.id)#space

        mc.setBlock(x0+3,y0+6,z0+3,85)
        mc.setBlock(x0+3,y0+5,z0+3,87)#set

        mc.setBlock(x0+2,y0+6,z0+3,0)
        mc.setBlock(x0+4,y0+6,z0+3,0)
        mc.setBlock(x0+3,y0+6,z0+2,0)
        mc.setBlock(x0+3,y0+6,z0+4,0)

        mc.setBlock(x0+2,y0+5,z0+3,50)
        mc.setBlock(x0+4,y0+5,z0+3,50)
        mc.setBlock(x0+3,y0+5,z0+2,50)
        mc.setBlock(x0+3,y0+5,z0+4,50)#torch

        for x in range(5):
            mc.setBlock(x0+1+x,y0+5,z0+1,98)
            mc.setBlock(x0+1+x,y0+5,z0+5,98)
            mc.setBlock(x0+1,y0+5,z0+1+x,98)
            mc.setBlock(x0+5,y0+5,z0+1+x,98)
        
        mc.setBlock(x0+5,y0+1,z0+1,156)
        mc.setBlock(x0+5,y0+1,z0+3,156)
        mc.setBlock(x0+5,y0+1,z0+2,85)
        mc.setBlock(x0+5,y0+2,z0+2,171)

        mc.setBlock(x0+2,y0+5,z0+4,30)
        mc.setBlock(x0+1,y0+4,z0+6,30)#cobweb


            
    def home(self):
        self.roof()
        self.wall()
        self.ground()
        self.decoration_home()  

houseposition = [pos.x+1,pos.y-1,pos.z]# DEFINE THE HOUSE POSITION


mh1 = SMITHY(houseposition)
#mh1.smithy()#if you use the smithy you will set the house at your place
mh1.clean()

#mh2 = PUMPKIN(houseposition)
#mh2.pumpkin()#if you use the smithy you will set the house at your place

#mh2.clean()

#mh3 = HOME(houseposition)
#mh3.clean()
#mh3.home()#if you use the smithy you will set the house at your place

'''
以上注释均为建房子的代码，clean为去掉房子的代码
'''