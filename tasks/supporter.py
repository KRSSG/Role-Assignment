import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint




class TSupporter(object):
	def __init__(self, arg):
		super(TSupporter, self).__init__()
		self.arg = arg
	def execute(self,state,bot_id,play_type=0):
		sParams = skills_union.SParam()
		sParams.GoToPointP.x = state.homePos[attacker_id].x+75*bot_id + 25
        sParams.GoToPointP.y = state.homePos[attacker_id].y+40*bot_id + 25
        sGoToPoint.execute(sParams, state, bot_id, pub)	 