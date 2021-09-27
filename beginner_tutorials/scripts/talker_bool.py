#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def talker_bool():
    pub = rospy.Publisher('chatter', Bool, queue_size=10)
    rospy.init_node('talker_bool', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        state =  False
        rospy.loginfo(state)
        pub.publish(state)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_bool()
    except rospy.ROSInterruptException:
        pass
