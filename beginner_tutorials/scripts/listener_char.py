#!/usr/bin/env python

import rospy
from std_msgs.msg import Char

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %c', data.data)

def listener_char():

    rospy.init_node('listener_char', anonymous=True)

    rospy.Subscriber('chatter', Char, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener_char()
