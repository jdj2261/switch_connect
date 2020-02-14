#-*- coding:utf-8 -*-
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ioutil.robocare_serial import RobocareSerial

port_close = False

class DataConversion():

    def __init__(self):
        print('DataConversion.__init__')
        # super(DataConversion, self).__init__()
        self.__is_connect = False
        self.__rs = RobocareSerial()
        self.waitPort()
        # if port_close ==True :
        #     print('close')


    def waitPort(self):
        while(True) : 
            self.__is_connect = self.__rs.open()
            if self.__is_connect == True :
                self.__rs.read()
                break
            time.sleep(1.0)
        print("스위치가 연결되었습니다.")





