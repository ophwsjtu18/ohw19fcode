import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

class PP():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class Statute():
    def __init__(self,mc):
        self.mc=mc
        self.pos=self.mc.player.getTilePos()

    def loadbinvox(self,a_statute):
        with open('./statutes/'+a_statute+'.binvox', 'rb') as f:
            model = binvox_rw.read_as_3d_array(f)
        return model

    def build(self,a_statute,pos):
        model=self.loadbinvox(a_statute)
        mc=self.mc
        #pos = self.mc.player.getTilePos()
        for y in range(model.dims[1]):
            print("layer y=", y)
            layer_data = model.data[y]
            stringlayer = ""
            for x in range(model.dims[0]):
                stringlayer = stringlayer + "\n"
                for z in range(model.dims[2]):
                    if model.data[x][y][z] == True:
                        stringlayer = stringlayer + '1'
                        mc.setBlock(pos.x + x, pos.y + z, pos.z + y, block.DIAMOND_BLOCK.id)
                    else:
                        stringlayer = stringlayer + '0'
                        mc.setBlock(pos.x + x, pos.y + z, pos.z + y, block.AIR.id)
            print(stringlayer)
