import binvox_rw
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

Material=[block.IRON_BLOCK.id,block.WOOD.id,block.SNOW_BLOCK.id]

with open('donut.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""                                                               #生成甜甜圈
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][y][z] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(pos.x+x,pos.y+20+y,pos.z+z,block.STONE.id)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(pos.x+x,pos.y+20+y,pos.z+z,block.AIR.id)
    print(stringlayer)

pat=[
[1,1,1,1,1,1,1,1,1,1],
[1,3,3,3,3,3,3,3,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,3,1,3,1,3,1],                                   #屋顶的花纹
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,3,3,3,3,3,3,3,1],
[1,1,1,1,1,1,1,1,1,1]]

def house(x0,y0,z0,M=block.SNOW_BLOCK.id,L=10,W=10,H=10,):
    for a in range(0,L):
        for c in range(0,W):
            for b in range(0,H):
                mc.setBlock(x0+a,y0+b,z0+c,M)                 #先填满
    for a in range(0,L-2):
        for c in range(0,W-2):
            for b in range(0,H-1):
                mc.setBlock(x0+1+a,y0+1+b,z0+1+c,0)           #再清除内部
    for a in range(0,L):
        for b in range(0,W):
            if pat[a][b]==1:
                mc.setBlock(x0+a,y0+H,z0+b,block.GLASS.id)        #天花板透明
            else:
                mc.setBlock(x0+a,y0+H,z0+b,block.DIAMOND_BLOCK.id)
    for a in range(1,3):
        x1=int((2*x0+L)/2)
        mc.setBlock(x1,y0+a,z0,0)                             #造个门
    x1=int(x0+L/4)
    y1=int(y0+H/2)
    mc.setBlock(x1,y1,z0,block.GLASS.id)                                   #开个窗户

house(pos.x,pos.y,pos.z,Material[0])
house(pos.x+15,pos.y,pos.z,Material[1])                         #造三个房子，状态不一样
house(pos.x-15,pos.y,pos.z,Material[2])

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "COM17" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
mc=Minecraft.create()
time.sleep(2)
#mc=Minecraft.create("10.163.80.195",4711)
action = "empty"
stayed_time=0

pos00=mc.player.getTilePos()
x00=pos00.x
y00=pos00.y                                                            #指引玩家回家
z00=pos00.z
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x="+str((x00+5))+ "y="+str((y00+1))+ " z="+str((z00)+4)+" for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==x00+5 and pos.y==y00+1 and pos.z==z00+4:
        mc.postToChat("welcome home")
        # action='1'
        # ser.write(action.encode())
        # time.sleep(1)
        # ser.write("y".encode())                                    #把这里的注释取消掉就可以播放音乐
        # time.sleep(1)
        # ser.write("g".encode())
        # time.sleep(1)
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(x00,y00,z00)
            stayed_time=0
    else:
        stayed_time=0