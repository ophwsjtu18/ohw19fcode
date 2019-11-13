# Author: Kang Huquan & Girafboy
# encoding:utf-8

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from song import Song
from model import Model
from house import House

mc=minecraft.Minecraft.create("127.0.0.3", 4711)


pos = mc.player.getTilePos()
house1 = House(mc,[pos.x, pos.y, pos.z])
house2 = House(mc,[pos.x+20, pos.y, pos.z])
house3 = House(mc,[pos.x+40, pos.y, pos.z])
house1.build()
house2.build()
house3.build()
model1 = Model(mc,'chiji.binvox')
model2 = Model(mc,'guidaopao.binvox')
model3 = Model(mc,'mickey__mouse_hoofd.binvox')
model1.build([pos.x, pos.y, pos.z+20])
model2.build([pos.x+20, pos.y, pos.z+20])
model3.build([pos.x+40, pos.y, pos.z+20])

song = Song()
while True:
    pos = mc.player.getTilePos()
    if house1.inHouse([pos.x, pos.y, pos.z]) or house3.inHouse([pos.x, pos.y, pos.z]):
        song.run('我爱北京天安门')
        print("Play song No.1")
    if house2.inHouse([pos.x, pos.y, pos.z]):
        song.run('新年好啊')
        print("Play song No.2")
