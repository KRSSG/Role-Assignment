import sys, os
import rospy
from krssg_ssl_msgs.msg import BeliefState
from krssg_ssl_msgs.msg import gr_Commands
from krssg_ssl_msgs.msg import Refree
from utils.config import *
from tactics import TGoalie
from tactics import TestTac
from tactics import TPosition
from tactics import TPrimaryDefender
from tactics import TLDefender
from tactics import TRDefender
from tactics import TDTP,TAttacker
from tactics import TTestIt
import math
from utils.geometry import Vector2D
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall

task_list = []
bot_id_list = []
marked = [0,0,0,0,0,0]
play_type

class GameAnalyser(object):
	def __init__(self, state):
		super(GameAnalyser, self).__init__(state)
		self.arg = arg
		self.home_yellow = state.isteamyellow

	#task 0
	def Defender(self,state,bot_id,point):
    	sParams = skills_union.SParam()
    	sParams.GoToPointP.x = point.x
	    sParams.GoToPointP.y = point.y

	    sGoToPoint.execute(sParams, state, bot_id, pub)

	def BallHandler(self,state,bot_id):
		#if it is a free kick we are taking
		global play_type
		if play_type == 0 :
			sParams = skills_union.SParam()	
			sGoToBall.execute(sParams, state, bot_id, pub)
			param = skills_union.SParam()
			param.KickToPointP.x = 4500       
            param.KickToPointP.y = 0
            param.KickToPointP.power = 7
            sKickToPoint.execute(param, state, self.bot_id, pub)
        #if we are defending a free kick
        if play_type == 1:
        	sParams = skills_union.SParam()
            ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
            sParams.GoToPointP.x = 0.3*ballPos.x + 0.7*4500
            sParams.GoToPointP.y = 0.3*ballPos.y 
            sGoToPoint.execute(sParams, state, bot_id, pub)	

    def marker (self,state,bot_id):
    	dis = 9999999
    	nearest_bot = 0
    	for i in xrange(len(state.awayPos)):
    		if not marked[i]:
    			dist=fabs(Vector2D(int(state.homePos[bot_id].x),int(state.homePos[bot_id].y)).dist(Vector2D(int(state.awayPos[i].x),int(state.awayPos[i].y))))
    			if dist < dis :
    				dist = dis
    				nearest_bot = i
		sParams = skills_union.SParam()
		sParams.GoToPointP.x = state.homePos[bot_id].x
        sParams.GoToPointP.y = state.homePos[bot_id].y 
        sGoToPoint.execute(sParams, state, bot_id, pub)	

    def supporter (self,state,bot_id,attacker_id):
    	sParams = skills_union.SParam()
		sParams.GoToPointP.x = state.homePos[attacker_id].x+75*bot_id + 25
        sParams.GoToPointP.y = state.homePos[attacker_id].y+40*bot_id + 25
        sGoToPoint.execute(sParams, state, bot_id, pub)	   	

    def supporter (self,state,bot_id):
    	pass

    def attacker (self,state,bot_id) :
    	pass

     def clearer (self,state,bot_id) :
     	pass

     def refree_callback(self,msg):
     	global play_type
     	if (self.home_yellow and msg.command == 8) or ((not self.home_yellow) and msg.command == 9) :
     		#our direct freekick
     		play_type = 0
     	elif msg.command == 8 or msg.command == 9 :
     		#their direct freekick
     		play_type = 1
     	elif (self.home_yellow and msg.command == 10) or ((not self.home_yellow) and msg.command == 11) :
     		#our indirect freekick
     		play_type = 2
     	elif msg.command == 10 or msg.command == 11 :
     		#their indirect free kick
     		play_type = 3
     	elif (self.home_yellow and msg.command == 6) or ((not self.home_yellow) and msg.command == 7) :
     		#our penalty
     		play_type = 4
     	elif msg.command == 6 or msg.command == 7 :
     		#their penalty
     		play_type = 5

	def select_tasks(self,state):
		global play_type , task_list , bot_id_list
		task_list.clear()
		bot_id_list.clear()
		if play_type == 1:
			task_list.append("BallHandler")
			task_list.append("clearer")
			task_list.append("marker")
			task_list.append("marker")
			task_list.append("defender")

def main():
    global pub
	object = GameAnalyser()    
    rospy.Subscriber('/belief_state', BeliefState, obj.select_tasks, queue_size=1000)
    rospy.Subscriber('/ref_data',Refree,refree_callback,queue_size=1000)
	rospy.spin()

if __name__=='__main__':
    # rospy.init_node('skill_py_node',anonymous=False)
    main()