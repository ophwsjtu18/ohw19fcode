from song_comled import sing
import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create("172.18.11.13",4711)
pos=mc.player.getTilePos()
#mc.player.setTilePos([0,0,0])#设置玩家坐标
#mc.setBlock(pos.x+3,pos.y,pos.z,41)#在一个地方放置方块，数字为材质ID，查看方法，F3+H松开，打开E背包
#"""
if(pos.x==0)sing()
for a in range(10):
    mc.setBlock(pos.x-a,pos.y,pos.z,89)
"""
    mc.setBlock(pos.x,pos.y,pos.z-a,89)
    mc.setBlock(pos.x-9,pos.y,pos.z-a,89)
    mc.setBlock(pos.x-a,pos.y,pos.z-9,89)
    
for aa in range(1000):
    for bb in range(1000):
        for cc in range(1000):
                mc.setBlock(pos.x+aa,pos.y+bb,pos.z+cc,383/62)
"""



    
    
