#-*- coding:utf-8 -*-

import time
import serial
from manages.ros_manage import RosManager

class RobocareSerialReader():
    def __init__(self, serial):
        self.__serial = serial
        print 'RobocareSerialReader : init'
        self.__is_end = False
        self.__result=''
        self.__rm = RosManager()

    def run(self, tmp):
        print 'RobocareSerialReader read start'
        
        while not self.__is_end:
            out = ''
            # receive_data = 'okok'
            while self.__serial.inWaiting() > 0:
                read_packet = bytearray(self.__serial.read(1))
                # out += str(hex(read_packet[0]))+' '
                out += format(read_packet[0], '02x')+' '
                # print(out)
                
            if out != '':
                self.__result = out.strip()
                # print(receive_data)
                if self.__result == '01 01 02 10 eb':
                    self.__rm.pub()

            time.sleep(0.1)

        print 'RobocareSerialReader read fin'

    def stop(self):
        self.__is_end = True

 
