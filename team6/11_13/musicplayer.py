import serial
import serial.tools.list_ports
import time
import csv

class arduino_run:

    def __init__(self,action="empty"):
        print ('hello')
        ports = list(serial.tools.list_ports.comports())
        print (ports)

        for p in ports:
            print (p[1])
            if "COM3" in p[1]:
                self.ser =serial.Serial(port=p[0])
            else :
                print ("No Arduino Device was found connected to the computer")
                
    def refreash(self,action):
        self.action=action
        
    def run(self):
        while self.action != "q":
            print ('q for quit,others for command')
            self.ser.write(self.action.encode())
            time.sleep(1)
"""
a=arduino_run()
a.refreash("1")
a.run()"""
