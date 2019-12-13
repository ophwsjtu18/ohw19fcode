import mcpi.minecraft as minecraft
import mcpi.block as block
from house import House
from musicplayer import *

mc=minecraft.Minecraft.create()
#mc.player.setTilePos([0,0,0])
pos=mc.player.getTilePos()
pos0=[]
pos0.append(pos.x)
pos0.append(pos.y)
pos0.append(pos.z)
mh1=House([pos.x,pos.y,pos.z],mc)
mh1.buildall()
#mh2=House([pos.x+20,pos.y,pos.z],mc,block.GOLD_BLOCK.id,block.GLASS.id)
#mh2.buildall()
#mh3=House([pos.x+40,pos.y,pos.z],mc,block.IRON_BLOCK.id,block.WOOD.id)
#mh3.buildall()

while (True):
    if(mh1.isInsideHouse()):
        mc.postToChat("Your're dead")


