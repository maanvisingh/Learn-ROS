#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener_int():

    rospy.init_node('listener_int', anonymous=True)

    rospy.Subscriber('chatter', Int16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener_int()
