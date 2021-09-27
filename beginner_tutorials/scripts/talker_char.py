#!/usr/bin/env python

import rospy
from std_msgs.msg import Char

def talker_char():
    pub = rospy.Publisher('chatter', Char, queue_size=10)
    rospy.init_node('talker_char', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ch =  '@'
        #rospy.loginfo(ord(ch))
        pub.publish(ord(ch))
        print(ch)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_char()
    except rospy.ROSInterruptException:
        pass
