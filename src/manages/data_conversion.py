#-*- coding:utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ioutil.robocare_serial import RobocareSerial
from manages.ros_manage import RosManager

class DataConversion():

    def __init__(self):
        print('DataConversion.__init__')
        # super(DataConversion, self).__init__()
        self.__send_data = '01 01 02 10 eb'
        self.__rs = RobocareSerial()
        # self.__rm = RosManager()

        self.__rs.open()
        self.__rs.read()

        # 프로토콜 정의
        """
        정상        :  01 01 02 10 EB
        체크섬 에러 :   01 0E 19 97 40
        데이터 에러 :   01 0E 05 05 E6
        """
        if receive_data == '01 01 02 10 eb':
            print(self.__send_data) 
            self.__rm.pub()
            self.__rs.write(self.__send_data, 0.1, 1)

        elif receive_data == '01 0E 19 97 40':
            self.__rs.write(self.__send_data, 0.1, 1)

        else :
            self.__rs.write(self.__send_data, 0.1, 1)