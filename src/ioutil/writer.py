#-*- coding:utf-8 -*-

import time
import serial

class RobocareSerialWriter():
    def __init__(self, serial, hex_str, duration=0.1, send_count=1):
        self.__serial = serial
        print 'RobocareSerialWriter : '+hex_str+', duration '+str(duration)+', count : '+str(send_count)
        self.__hex_str = hex_str.replace(' ', '')
        self.__duration = duration
        self.__send_count = send_count
        self.__is_end = False

    def run(self, tmp):
        if( len(self.__hex_str) % 2 == 1 ):
            print 'input length must be even size'
        else:
            input_count = len(self.__hex_str) / 2 
            default_elements = []
            for i in range(0, input_count):
                default_elements.append(0)
            packet = bytearray(default_elements)

            for i in range(0, input_count):
                hex_str = str(self.__hex_str[i*2:i*2+2])
                # print 'hex_str : [' + hex_str + ']'
                packet[i] = hex_str.decode('hex')
            count = 0
            print 'RobocareSerialWriter run start'
            while self.__send_count > count and not self.__is_end:
            # while True:
                # print 'write count : '+str(count)
                self.__serial.write(packet)
                count += 1
                time.sleep(self.__duration)
            print 'RobocareSerialWriter run fin'
    
    def is_end(self):
        return self.__is_end

    def stop(self):
        self.__is_end = True
