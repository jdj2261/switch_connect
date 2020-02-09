#-*- coding:utf-8 -*-
import rospy

from std_msgs.msg import Bool

class RosManager():

    def __init__(self):
        self.__wakeup_pub = rospy.Publisher('/is_wakeup', Bool, queue_size=1)

    def pub(self):
        is_wakeup = Bool()
        is_wakeup = True
        self.__wakeup_pub.publish(is_wakeup)