#!/usr/bin/env python


from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import math
import rospy
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)




def moveTurtle():
	rate = rospy.Rate(70.0)	# Duration of the command rosply.sleep => 70 was the duration that gave the smoother 8 shape
	
	
	T = input('\nEnter a value for T (1/Hz): ') 	# for T=5 we should have around 354 msgs for a full lap
 
	Pi = math.pi					# define the value of PI
		
	t0 = rospy.get_time()				# get starting time for the script to 
	
	while not rospy.is_shutdown():	
		

		t = rospy.get_time() - t0		# make sure that t always starts 0 instead of getting the computer internal clock 


		vX = (12 * Pi * math.cos(4 * Pi * t / T)) / T			# velocity on the X axis
		vY = (6 * Pi * math.cos(2 * Pi * t / T)) / T			# velocity on the Y axis
		
		aX = (-48 * Pi * Pi * math.sin(4 * Pi * t / T)) / (T * T)	# aceleration on the X axis
		aY = (-12 * Pi * Pi * math.sin(2 * Pi * t / T)) / (T * T)	# aceleration on the Y axis
		
		v = math.sqrt(vX * vX + vY * vY)				# straight velocity calculation

		omega = (vX * aY - vY * aX) / (vX * vX + vY * vY)		# angular velocity calculation

		command = Twist()		# create a new msg Twist to be published
		command.linear.x = v		# insert the velocity on X (front of the turtle)
		command.linear.y = 0		
		command.linear.z = 0
		command.angular.x = 0
		command.angular.y = 0
		command.angular.z = omega	# insert angular velocity to steer the turtle
		pub.publish(command)		# publish the command
		rate.sleep()			# sleep for the rate defined at the top of the code



if __name__ == '__main__':
	try:
		rospy.wait_for_service('turtle1/teleport_absolute')			# wait for the turtle simulator start running
		turtle_sp = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute) 
		turtle_sp = (20,5,0)		#set turtle initial position
		rospy.init_node('steering_turtle', anonymous=True) # init node
		moveTurtle()
	except rospy.ROSInterruptException: pass

		

