import binvox_rw
import mcpi.minecraft as minecraft
import serial
import serial.tools.list_ports
import time

with open('chair.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

position=list(pos)
position1=list(range(3))
position2=list(range(3))
position3=list(range(3))
position4=list(range(3))
for i in range(3):
    position1[i]=list(pos)[i]+25
    position2[i]=list(pos)[i]-25
    position3[i]=list(pos)[i]-50
    position4[i]=list(pos)[i]


position1[1]=list(pos)[1]
position2[1]=list(pos)[1]
position3[1]=list(pos)[1]
position4[1]=list(pos)[1]+20

class House():
    def __init__(self,data):
        self.data=data
        
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0+x,y0+8,z+z0,57)
                    
    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(9):
            for z in range(11):
                mc.setBlock(x0,y+y0,z+z0,41)
                mc.setBlock(x0+10,y+y0,z+z0,41)
        for y in range(9):
            for x in range(10):
                mc.setBlock(x0+x+1,y+y0,z0,41)
                mc.setBlock(x0+x+1,y+y0,z0+10,41)
                    
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(5):
            mc.setBlock(x0+4,y+y0,z0,0)
            mc.setBlock(x0+5,y+y0,z0,0)

    def window(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(2):
            mc.setBlock(x0+7,y+y0+4,z0,20)
            mc.setBlock(x0+8,y+y0+4,z0,20)
    def status(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for i in range(len(model.data)):
            for j in range(len(model.data[i])):
                for k in range(len(model.data[i][j])):
                    if model.data[i][j][k] == True:
                        mc.setBlock(x0+k,y0+j,z0+i,41)
                    else:
                        mc.setBlock(x0+k,y0+j,z0+i,0)
    
    def return_position(self):
        list_position = []
        for i in range(3):
            list_position.append(self.data[i])
        return list_position
        




                    

mh=House(position)
mh.wall()
mh.roof()
mh.door()
mh.window()
mh1=House(position1)
mh1.wall()
mh1.roof()
mh1.door()
mh1.window()
mh2=House(position2)
mh2.wall()
mh2.roof()
mh2.door()
mh2.window()
length =10
height =8
width = 10
mh3=House(position4)
mh3.status()

list_position1 = []
list_position2 = []
list_position3 = []

list_position1 = mh1.return_position()
list_position2 = mh2.return_position()
list_position3 = mh3.return_position()

mc_now = minecraft.Minecraft.create()


ports = list(serial.tools.list_ports.comports())
print(ports)
for o in ports:
    print (p[1])
    if "SERIAL" in p[1]:
        ser = serial.Serial(port = p[0])
    else:
        print("No Arduino Device was found connected to the computer")
time.sleep(2)

while (1):
    pos_now = mc_now.player.getTilePos()
    list_position = []
    list_position.append(pos_now.x)
    list_position.append(pos_now.y)
    list_position.append(pos_now.z)
    return_for_arduino = 0

    if list_position[0] >= list_position1[0] and list_position[0] <= list_position1[0]+length:
        if list_position[1] >= list_position1[1] and list_position[1] <= list_position1[1]+height:
            if list_position[2] >= list_position1[2] and list_position[2] <= list_position1[2]+width:
                return_for_arduino = 1
                print(return_for_arduino)
    
    if list_position[0] >= list_position2[0] and list_position[0] <= list_position2[0]+length:
        if list_position[1] >= list_position1[1] and list_position[1] <= list_position2[1]+height:
            if list_position[2] >= list_position2[2] and list_position[2]<= list_position2[0]+width:
                return_for_arduino = 2
                print(return_for_arduino)
    if list_position[0] >= list_position3[0] and list_position[0] <= list_position3[0]+length:
        if list_position[1] >= list_position3[1] and list_position[1] <= list_position3[1]+height:
            if list_position[2] >= list_position3[2] and list_position[2] <= list_position3[2]+width:
                return_for_arduino = 3
                print(return_for_arduino)

    

    return_for_arduino_char = ''
    return_for_arduino_char = str(return_for_arduino)
    ser.write(return_for_arduino_char.encode())
    time.sleep(1)
