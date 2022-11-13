#!/usr/bin/python3

'''
    An example code block for development.
    unfinished. Not complied by cmake.
'''
import sys

# the python pkg for ros functionalities
import rospy
# import the msg type
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


class position:
    # publc
    name = ''
    age = 0
    # privat
    __weight = 0
    # konstruktor
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w


    def get_postionspeak(self):

        print("%s 说: 我 %d 岁。" %(self.name,self.age))

    def set_pisition(self):

        