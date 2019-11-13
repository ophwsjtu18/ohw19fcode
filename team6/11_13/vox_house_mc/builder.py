import myhouse
import bvox
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create()

myhouse.mc=mc
bvox.mc=mc
myhouse.all_build()

m1=bvox.loadVox('donut.binvox')
bvox.buildVox(m1,[-5,5,20],block.DIAMOND_BLOCK.id)

print(myhouse.mh.data)
print(myhouse.mh2.data)
print(myhouse.mh3.data)
while(1):
    time.sleep(0.5)
    p=mc.player.getTilePos()
    #print(p)
    if myhouse.mh.inhouse(p):
        print('mh1')
    
    if myhouse.mh2.inhouse(p):
        print('mh2')
    
    if myhouse.mh3.inhouse(p):
        print('mh3')
