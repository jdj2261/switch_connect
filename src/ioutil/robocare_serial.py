#-*- coding:utf-8 -*-

import sys
import rospy
import time
import serial
import thread

from ioutil.reader import RobocareSerialReader
from ioutil.writer import RobocareSerialWriter

class RobocareSerial():

    def __init__(self):
        self.__reader = None
        self.__writer = None
        self.__serial = None

    def open(self):
        try:
            self.__serial = serial.Serial(
                port='/dev/leonardo',
                baudrate=9600
            )

        except:
            print(u' 포트를 여는 데 실패했습니다.')
           
            return False
        return True

    def write(self, input, duration=0.1, count=1):
        if self.__serial != None:
            if self.__serial.is_open:
                if self.__writer != None:
                    if not self.__writer.is_end():
                        self.__writer.stop()
                        time.sleep(0.1)
                self.__writer = RobocareSerialWriter(serial=self.__serial, hex_str=input, duration=duration, send_count=count)
                thread.start_new_thread(self.__writer.run, ("", ))
            else:
                print(u'포트가 연결이 되어 있는지 확인해 주세요')
        else:
            print(u'포트가 연결이 되어 있는지 확인해 주세요')

    def read(self):
        self.__reader = RobocareSerialReader(serial=self.__serial)
        thread.start_new_thread(self.__reader.run, ("", ))

    def close(self):
        self.stop()
        time.sleep(0.2)
        self.__serial.close()

    def stop(self):
        if self.__reader != None:
            self.__reader.stop()
        if self.__writer != None:
            self.__writer.stop()

