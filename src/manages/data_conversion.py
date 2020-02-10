#-*- coding:utf-8 -*-
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ioutil.robocare_serial import RobocareSerial

class DataConversion():

    def __init__(self):
        print('DataConversion.__init__')
        # super(DataConversion, self).__init__()
        self.__send_data = '01 01 02 10 eb'
        self.__rs = RobocareSerial()

        self.__rs.open()
        self.__rs.read()
