#!/usr/bin/env python

from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import rospy
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)




def moveTurtle():
	rate = rospy.Rate(5.0)	
	
	while not rospy.is_shutdown():
		command = Twist()
	
		command.linear.x = 10
		command.linear.y = 0
		command.linear.z = 0
		command.angular.x = 0
		command.angular.x = 0
		command.angular.x = 0
		print '\nPublishing'
		pub.publish(command)
		rate.sleep()



if __name__ == '__main__':
	try:
		rospy.wait_for_service('turtle1/teleport_absolute')
		turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
		turtle_sp = (3.54,5.54,0)
		rospy.init_node('steering_turtle', anonymous=True)
		moveTurtle()
	except rospy.ROSInterruptException: pass
		
	
