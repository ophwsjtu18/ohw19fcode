import serial
import serial.tools.list_ports
import time
import csv

class Song():
    def __init__(self):
        print ('hello')
        ports = list(serial.tools.list_ports.comports())
        print (ports)

        self.songs={}
        for p in ports:
            print (p[1])
            if "SERIAL" in p[1]:
                self.ser=serial.Serial(port=p[0])
            else:
                print ("No Arduino Device was found connected to the computer")

        with open("song.csv",encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                self.songs[row[0]] = row[1:]
        print(self.songs)
        time.sleep(2)

    def run(self, action):
        for ch in self.songs[action]:
            self.ser.write(ch.encode())
            self.ser.write(','.encode())
            time.sleep(0.25)
            
