#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def talker_int():
    pub = rospy.Publisher('chatter', Int16, queue_size=10)
    rospy.init_node('talker_int', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        number =  1234
        rospy.loginfo(number)
        pub.publish(number)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_int()
    except rospy.ROSInterruptException:
        pass
