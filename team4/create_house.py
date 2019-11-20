import binvox_rw

with open('chair.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

import mcpi.minecraft as minecraft
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
    def status(self):
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
length =10
height =8
width = 10
mh3=House(position4)
mh3.status()
