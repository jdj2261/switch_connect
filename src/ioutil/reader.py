#-*- coding:utf-8 -*-

import sys
import os
import time
import serial
from manages.ros_manage import RosManager
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from ioutil.robocare_serial import RobocareSerial

class RobocareSerialReader():

    def __init__(self, serial):
        self.__serial = serial
        print 'RobocareSerialReader : init'
        self.__is_end = False
        self.__result=''
        self.__rm = RosManager()
        self.__receive_data  = '01 01 02 10 eb'
        # self.__close = False
        port_close = False

    def run(self, tmp):
        print 'RobocareSerialReader read start'
        
        while not self.__is_end:

            out = ''
            
            try:
                while self.__serial.inWaiting() > 0:
                    read_packet = bytearray(self.__serial.read(1))
                    # out += str(hex(read_packet[0]))+' '
                    out += format(read_packet[0], '02x')+' '
                    # print(out)
                if out != '':
                    self.__result = out.strip()
                    # print(receive_data)
                    if self.__result ==  self.__receive_data:
                        print(u"press button")
                        self.__rm.wakeup_pub()

                time.sleep(0.1)
            except:
                self.reconect()

        print 'RobocareSerialReader read fin'
    
    def reconect(self):

        try:
            self.__serial = serial.Serial(
                port='/dev/leonardo',
                baudrate=9600
            )
            print("스위치가 재 연결되었습니다.")

        except:
            print(u' 포트를 다시 연결해 주세요')
        time.sleep(1)

    def stop(self):
        self.__is_end = True

 
