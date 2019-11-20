from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)


while True:
    time.sleep(0.5) 
    if mh0.isinsidehouse():
        for a in []:
            ser.write(0)
            time.sleep(3)
    if mh1.isinsidehouse():
        for a in []:
            ser.write(1)
            time.sleep(3)
    if mh2.isinsidehouse():
        for a in []:
            ser.write(2)
            time.sleep(3)

    else:
        stayed_time=0

