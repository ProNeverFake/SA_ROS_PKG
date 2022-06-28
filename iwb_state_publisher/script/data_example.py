
#!/usr/bin/python3

import sys

# the python pkg for ros functionalities
import rospy
# import the msg type
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


class position:
   
    # privat
    __position = ''
    __weight = 0
    # konstruktor
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    # publc
    def get_postionspeak(self):

        pass

    def set_pisition(self):

        pass