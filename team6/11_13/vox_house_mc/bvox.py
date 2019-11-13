import numpy as np
import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

def loadVox(path):
    with open(path,"rb") as f:
        m=binvox_rw.read_as_3d_array(f)
    return m

def buildVox(model,ordp,block):
    x0=ordp[0]
    y0=ordp[1]
    z0=ordp[2]

    for x in range(model.dims[0]):
        for y in range(model.dims[1]):
            for z in range(model.dims[2]):
                if model.data[x][y][z]:
                    mc.setBlock(x0+x,y0+y,z+z0,block)
                else:
                    mc.setBlock(x0+x,y0+y,z+z0,0)

def clear(p,s):
    for x in range(s):
        for y in range(s):
            for z in range(s):
                mc.setBlock(p[0]+x,p[1]+y,p[2]+z,0)

if __name__=='__main__':
    mc=Minecraft.create()
    _ordp=[-5,5,60]
    m1=loadVox('donut.binvox')
    buildVox(m1,_ordp,block.DIAMOND_BLOCK.id)
