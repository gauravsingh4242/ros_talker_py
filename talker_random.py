#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import random


def talker():
	pub = rospy.Publisher('random', Int32, queue_size=10)
	rospy.init_node('talker_random', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = random.randint(100, 10000)
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
