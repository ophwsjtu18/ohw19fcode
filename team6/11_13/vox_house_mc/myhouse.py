from mcpi.minecraft import Minecraft
import mcpi.block as block
#pat=[[0]*11]*11
pat1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
pat2=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0], 
    [0, 1, 1, 1, 0, 0, 0, 2, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
pat3=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0], 
    [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 2, 0, 0, 2, 1, 2, 0, 0], 
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]

house_blocks=[block.GLASS.id,block.DIAMOND_BLOCK.id,block.GOLD_BLOCK.id]

class MyHouse():
    def __init__(self,data,pat):
        self.data=data
        self.pat=pat
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0-10+x,y0+6,z+z0-5,house_blocks[self.pat[x][z]])
    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for y in range(6):
                            
                if (x in range(2,4) or x in range(7,9)) and y in range(3,5):
                    mid=block.GLASS.id
                else:
                    mid=block.WOOD.id
                            
                mc.setBlock(x0-10+x,y0+y,z0-5,mid)
                mc.setBlock(x0-10+x,y0+y,z0+5,mid)
        for z in range(11):
            for y in range(6):
                if (z in range(2,4) or z in range(7,9)) and y in range(3,5):
                    mid=block.GLASS.id
                else:
                    mid=block.WOOD.id
                mc.setBlock(x0-10,y0+y,z0-5+z,mid)
                mc.setBlock(x0,y0+y,z0-5+z,mid)
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(2):
            mc.setBlock(x0-4,y0+y,z0-5,0)
            mc.setBlock(x0-5,y0+y,z0-5,0)
            mc.setBlock(x0-6,y0+y,z0-5,0)

    def ground(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0-10+x,y0-1,z+z0-5,block.DIRT.id)
    def clear_ground(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0-10+x,y0-1,z+z0-5,0)
                
    def build_all(self):
        self.roof()
        self.wall()
        self.door()
        self.ground()
    def clear(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for y in range(8):
                for z in range(11):
                    mc.setBlock(x0-10+x,y0+y,z+z0-5,0)
    def inhouse(self,p):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        return p.x>x0-10 and p.x<x0 and p.z>z0-5 and p.z<z0+5 and p.y>=y0 and p.y<y0+6


mh=MyHouse([-20,5,60],pat1)
mh2=MyHouse([-5,5,60],pat2)
mh3=MyHouse([10,5,60],pat3)

def all_clear(ground=0):
    mh.clear()
    mh2.clear()
    mh3.clear()
    if ground:
        mh.clear_ground()
        mh2.clear_ground()
        mh3.clear_ground()

def all_build():
    mh.build_all()
    mh2.build_all()
    mh3.build_all()
            
if __name__=='__main__':
    mc=Minecraft.create()
    p=mc.player.getTilePos()
    print(p)
    #mh=MyHouse([p.x,p.y,p.z])
    all_build()
