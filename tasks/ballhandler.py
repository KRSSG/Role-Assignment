import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint


class ballHandler(object):
	def __init__(self, arg):
		super(ballHandler, self).__init__()
		self.arg = arg
	def execute(self,state,bot_id,play_type=0):
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