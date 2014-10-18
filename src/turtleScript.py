#!/usr/bin/env python


from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import math
import rospy
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)




def moveTurtle():
	rate = rospy.Rate(70.0)	
	
	
	T = input('\n Enter a value for T (1/Hz): ') # for T=5 we should have around 354 msgs for a full lap
 
	Pi = math.pi
	
	t0 = rospy.get_time()
	
	while not rospy.is_shutdown():
		

		t = rospy.get_time() - t0

		
		#print '\nt = ', t		

		vX = (12 * Pi * math.cos(4 * Pi * t / T)) / T
		vY = (6 * Pi * math.cos(2 * Pi * t / T)) / T
		
		aX = (-48 * Pi * Pi * math.sin(4 * Pi * t / T)) / (T * T)
		aY = (-12 * Pi * Pi * math.sin(2 * Pi * t / T)) / (T * T)
		
		v = math.sqrt(vX * vX + vY * vY)

		omega = (vX * aY - vY * aX) / (vX * vX + vY * vY)

		command = Twist()	
		command.linear.x = v
		command.linear.y = 0
		command.linear.z = 0
		command.angular.x = 0
		command.angular.y = 0
		command.angular.z = omega
		#print '\nPublishing'
		pub.publish(command)
		rate.sleep()



if __name__ == '__main__':
	try:
		rospy.wait_for_service('turtle1/teleport_absolute')
		turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
		turtle_sp = (20,5,0)
		rospy.init_node('steering_turtle', anonymous=True)
		moveTurtle()
	except rospy.ROSInterruptException: pass
		

