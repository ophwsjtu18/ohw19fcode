import binvox_rw
import mcpi.block as block

class Model():
    def __init__(self, mc, binvox_pathname):
        self.mc = mc
        with open(binvox_pathname, 'rb') as f:
            self.model = binvox_rw.read_as_3d_array(f)
        print(self.model.dims)
        print(self.model.scale)
        print(self.model.translate)

    def build(self, pos):
        for y in range(self.model.dims[1]):
            print("layer y=", y)
            layer_data=self.model.data[y]
            stringlayer=""
            for x in range(self.model.dims[0]):
                stringlayer=stringlayer+"\n"
                for z in range(self.model.dims[2]):
                    if self.model.data[x][y][z] == True:
                        stringlayer=stringlayer+'1'
                        self.mc.setBlock(pos[0]+x,pos[1]+z,pos[2]+y,block.STONE.id)
                    else:
                        stringlayer=stringlayer+'0'
                        self.mc.setBlock(pos[0]+x,pos[1]+z,pos[2]+y,block.AIR.id)
            print(stringlayer)
