import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint




class TMarker(object):
	def __init__(self, arg):
		super(TMarker, self).__init__()
		self.arg = arg
	def execute(self,state,bot_id,play_type=0):
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