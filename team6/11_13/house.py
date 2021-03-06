import mcpi.minecraft as minecraft
import mcpi.block as block
from statute import *
import random



class House():
    def __init__(self,data,mc,wall_mt=57,rf_mt=89):
        self.data=data
        self.mc=mc
        self.wall_mt=wall_mt
        self.rf_mt=rf_mt
        self.x0=self.data[0]
        self.y0=self.data[1]
        self.z0=self.data[2]
    def buildWall(self,wall_mt):
        for i in range(11):
            for j in range(6):
                self.mc.setBlock(self.x0+i,self.y0+j,self.z0,wall_mt)
        for i in range(11):
            for j in range(6):
                self.mc.setBlock(self.x0,self.y0+j,self.z0+i,wall_mt)
        for i in range(11):
            for j in range(6):
                self.mc.setBlock(self.x0+10,self.y0+j,self.z0+i,wall_mt)
        for i in range(11):
            for j in range(6):
                self.mc.setBlock(self.x0+i,self.y0+j,self.z0+10,wall_mt)
        for i in range(3):
            self.mc.setBlock(self.x0+5,self.y0+i,self.z0,block.AIR.id)
            self.mc.setBlock(self.x0+6,self.y0+i,self.z0,block.AIR.id)
        for i in range(2):
            for j in range(2):
                    self.mc.setBlock(self.x0,self.y0+2+i,self.z0+5+j,20)
    def roof(self,rf_mt):
        for i in range(6):
            for j in range (6-i):
                for k in range(11):
                    self.mc.setBlock(self.x0+5+j,self.y0+6+i,self.z0+k,rf_mt)
                    self.mc.setBlock(self.x0+5-j,self.y0+6+i,self.z0+k,rf_mt)
    def buildall(self):
        self.buildWall(self.wall_mt)
        self.roof(self.rf_mt)
        pos=PP(self.x0,self.y0,self.z0-100)
        self.statute=Statute(self.mc)
        self.statute.build(str(random.randint(1,3)),pos)

    def isInsideHouse(self):
        pos=self.mc.player.getTilePos()
        if pos.x>=self.x0 and pos.x<=self.x0+11 and pos.z>=self.z0 and pos.z<=self.z0+11:
            self.mc.postToChat("welcome home")
            return True


