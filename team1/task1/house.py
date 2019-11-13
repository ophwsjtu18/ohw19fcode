import mcpi.minecraft as minecraft
import mcpi.block as block

class House():
    def __init__(self, mc, data):
        self.mc = mc
        self.data = data
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        pat = [[1,1,1,1,1,1,1,1,1,1,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1]]
        for x in range(11):
            for z in range(11):
                if pat[x][z] == 0:
                    self.mc.setBlock(x-11+x0, y0+20, z-11+z0, block.GLASS.id)
                elif pat[x][z] == 2:
                    self.mc.setBlock(x-11+x0, y0+20, z-11+z0, block.DIAMOND_BLOCK.id)
                else:
                    self.mc.setBlock(x-11+x0, y0+20, z-11+z0, block.GOLD_BLOCK.id)


    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(20):
            for x in range(11):
                self.mc.setBlock(x0-11+x, y0+y, z0, block.GRASS.id)
                self.mc.setBlock(x0-11+x, y0+y, z0-11, block.GRASS.id)
            for z in range(11):
                self.mc.setBlock(x0, y0+y, z-11+z0, block.GRASS.id)
                self.mc.setBlock(x0-11, y0+y, z-11+z0, block.GRASS.id)

    def build(self):
        self.wall()
        self.roof()

    def inHouse(self, pos):
        if(pos[0]>self.data[0] and pos[0] < self.data[0]+11
           and pos[0]>self.data[0] and pos[0] < self.data[0]+11
           and pos[0]>self.data[0] and pos[0] < self.data[0]+11):
            return True
        else:
            return False
            

