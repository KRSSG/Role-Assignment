import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint




class TDefender(object):
	def __init__(self, arg):
		super(TDefender, self).__init__()
		self.arg = arg
	def execute(self,state,bot_id,point):
		sParams = skills_union.SParam()
    	sParams.GoToPointP.x = point.x
	    sParams.GoToPointP.y = point.y

	    sGoToPoint.execute(sParams, state, bot_id, pub)