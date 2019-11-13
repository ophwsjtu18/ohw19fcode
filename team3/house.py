import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()


""" with open('D:\\python code\\binvox-rw-py\\donut.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
#print(model.dims)
#print(model.scale)
#print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][y][z] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.STONE.id)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)
    print(stringlayer) """


place=[pos.x,pos.y,pos.z]

class house():
    def __init__(self,data,load):
        self.data=data
        self.load=load

    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                for y in range(11):
                    mc.setBlock(x+x0,y+y0,z+z0,block.STONE.id)
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
               mc.setBlock(x0+x,y0+11,z0+z,block.GLOWSTONE_BLOCK.id)

    def diaoxiang(self,load):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        with open(load, 'rb') as f:
            model = binvox_rw.read_as_3d_array(f)
#print(model.dims)
#print(model.scale)
#print(model.translate)
#print(model.data)

        for y in range(model.dims[1]):
            print("layer y=",y)
            layer_data=model.data[y]
            stringlayer=""
            for x in range(model.dims[0]):
                stringlayer=stringlayer+"\n"
                for z in range(model.dims[2]):
                    if model.data[x][y][z] == True:
                        stringlayer=stringlayer+'1'
                        mc.setBlock(x0+x,y0+25+y,z0+z,block.STONE.id)
                    else:
                        stringlayer=stringlayer+'0'
                        mc.setBlock(x0+x,y0+25+y,z0+z,block.AIR.id)
            print(stringlayer)


    def build(self):
        self.wall()
        self.window()
        self.door()
        self.fire()
        self.diaoxiang()
    def singasong(self):
    def isinsidehouse(self):


         

mh0=house (place,'D:\\python code\\binvox-rw-py\\donut.binvox')
place1=[pos.x+40,pos.y,pos.z]
place2=[pos.x-40,pos.y,pos.z]
mh1=house (place1,'D:\\python code\\binvox-rw-py\\tanke.binvox')
mh2=house (place2,'D:\\python code\\binvox-rw-py\\ufo.binvox')
mh0.build()
mh1.build()
mh2.build()