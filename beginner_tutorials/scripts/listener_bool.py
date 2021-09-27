#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener_bool():

    rospy.init_node('listener_Bool', anonymous=True)

    rospy.Subscriber('chatter', Bool, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener_bool()
