import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

class Statute:
    def __init__(self,mc):
        self.mc=mc
        self.pos=self.mc.player.getTilePos()

    def loadbinvox(self,a_statute):
        with open(a_statute+'.binvox', 'rb') as f:
            model = binvox_rw.read_as_3d_array(f)
        return model

    def build(self,a_statute,pos=self.pos):
        model=self.loadbinvox(a_statute)
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
                        mc.setBlock(pos.x + x, pos.y + y, pos.z + z, block.DIAMOND_BLOCK.id)
                    else:
                        stringlayer = stringlayer + '0'
                        mc.setBlock(pos.x + x, pos.y + y, pos.z + z, block.AIR.id)
            print(stringlayer)
