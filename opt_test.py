
"""
This is a test case file
Test cases are generated using "random"
The functions in this file have the same structures as in optimal_assignment.py 
"""

import sys
import rospy
from krssg_ssl_msgs.msg import BeliefState
from krssg_ssl_msgs.msg import gr_Commands
from utils.geometry import Vector2D
from utils.config import *
from optimalAssignment import *


botL = [1,2,3,4,5]
taskD = { 't1': Vector2D(500,500), 't2': Vector2D(1000,1000), 't3': Vector2D(2000,2000) }

obj = optimalAssignment(state, botL, taskD) 
print obj.decider(botL, taskD)

