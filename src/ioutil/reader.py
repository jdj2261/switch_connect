#-*- coding:utf-8 -*-

import time
import serial

class RobocareSerialReader():
    def __init__(self, serial):
        self.__serial = serial
        print 'RobocareSerialReader : init'
        self.__is_end = False
        self.__result=''

    def run(self):
        print 'RobocareSerialReader read start'
        global receive_data
        while not self.__is_end:
            out = ''
            # receive_data = 'okok'
            while self.__serial.inWaiting() > 0:
                read_packet = bytearray(self.__serial.read(1))
                # out += str(hex(read_packet[0]))+' '
                out += format(read_packet[0], '02x')+' '
                # print(out)
                
            if out != '':
                self.__result = out
                receive_data = out.strip()
                print(out)
                

            if out == '01 01 02 10 eb ':
                pass

            time.sleep(0.1)

        print 'RobocareSerialReader read fin'

    def stop(self):
        self.__is_end = True

 
